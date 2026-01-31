import json
from pathlib import Path
from typing import List, Dict

from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

from config import (
    OPENAI_API_KEY,
    MODEL_NAME,
    MAX_TURNS_TO_KEEP,
    MAX_OUTPUT_TOKENS,
    TEMPERATURE,
)

# Project root directory
ROOT = Path(__file__).parent

# Paths for prompt template and conversation memory
PROMPT_PATH = ROOT / "prompts" / "system_prompt.txt"
MEMORY_PATH = ROOT / "memory" / "history.json"


def load_system_prompt() -> str:
    """Load the system prompt template from file."""
    return PROMPT_PATH.read_text(encoding="utf-8").strip()


def load_history() -> List[Dict]:
    """Load conversation history from JSON file."""
    if not MEMORY_PATH.exists():
        return []
    try:
        data = json.loads(MEMORY_PATH.read_text(encoding="utf-8"))
        return data if isinstance(data, list) else []
    except Exception:
        # If the file is corrupted or invalid, start with empty history
        return []


def save_history(history: List[Dict]) -> None:
    """Save conversation history to JSON file."""
    MEMORY_PATH.parent.mkdir(parents=True, exist_ok=True)
    MEMORY_PATH.write_text(
        json.dumps(history, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )


def trim_history(history: List[Dict], max_turns: int) -> List[Dict]:
    """
    Keep only the most recent messages to limit context size
    and reduce token usage.
    """
    if max_turns <= 0:
        return []
    return history[-max_turns:]


def build_messages(
    system_prompt: str,
    business_context: str,
    role: str,
    history: List[Dict],
    user_message: str,
):
    """
    Build the message list for the LLM call, including:
    - system prompt
    - business context
    - selected role
    - recent conversation history
    - current user message
    """
    system_block = f"""{system_prompt}

BUSINESS_CONTEXT:
{business_context}

ROLE: {role}
"""
    messages = [SystemMessage(content=system_block)]

    # Add previous conversation turns
    for item in history:
        if item.get("type") == "human":
            messages.append(HumanMessage(content=item.get("content", "")))
        elif item.get("type") == "ai":
            messages.append(AIMessage(content=item.get("content", "")))

    # Add the latest user message
    messages.append(HumanMessage(content=user_message))
    return messages


def main():
    """Run the CLI-based AI Business Assistant."""
    if not OPENAI_API_KEY:
        print("ERROR: OPENAI_API_KEY not found. Create a .env file with OPENAI_API_KEY=...")
        return

    print("=== AI Business Assistant (CLI) ===")
    print("Type 'exit' or 'quit' to stop.\n")

    # Step 1: Collect business context
    print("Step 1/2: Paste business description (context).")
    print("Include products, services, hours, policies, etc.")
    print("Tip: Keep it short during development to reduce cost.")
    business_context = input("\nBUSINESS_CONTEXT> ").strip()
    if not business_context:
        business_context = "Small business. No additional context provided."

    # Step 2: Select assistant role
    print("\nStep 2/2: Choose role: sales / support / manager")
    role = input("ROLE> ").strip().lower()
    if role not in {"sales", "support", "manager"}:
        role = "support"

    system_prompt = load_system_prompt()
    history = load_history()

    # Initialize LLM client
    llm = ChatOpenAI(
        model=MODEL_NAME,
        api_key=OPENAI_API_KEY,
        temperature=TEMPERATURE,
        max_tokens=MAX_OUTPUT_TOKENS,
    )

    # Main chat loop
    while True:
        user_message = input("\nYOU> ").strip()
        if user_message.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break
        if not user_message:
            continue

        # Trim history to control context size
        history = trim_history(history, MAX_TURNS_TO_KEEP)

        messages = build_messages(
            system_prompt,
            business_context,
            role,
            history,
            user_message,
        )

        try:
            response = llm.invoke(messages)
            assistant_text = response.content.strip()
        except Exception as e:
            assistant_text = f"ERROR calling model: {e}"

        print(f"\nASSISTANT> {assistant_text}")

        # Save conversation turn
        history.append({"type": "human", "content": user_message})
        history.append({"type": "ai", "content": assistant_text})
        save_history(history)


if __name__ == "__main__":
    main()
