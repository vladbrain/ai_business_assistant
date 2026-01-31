import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

from config import OPENAI_API_KEY, MODEL_NAME, MAX_OUTPUT_TOKENS, TEMPERATURE


def build_system_message(business_context: str, role: str) -> str:
    """Build the system message including business context and role."""
    system_prompt = st.session_state.get("system_prompt_text", "").strip()

    return f"""{system_prompt}

BUSINESS_CONTEXT:
{business_context}

ROLE: {role}
""".strip()


def init_state():
    """Initialize Streamlit session state variables."""
    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "business_context" not in st.session_state:
        st.session_state.business_context = ""

    if "role" not in st.session_state:
        st.session_state.role = "support"

    if "system_prompt_text" not in st.session_state:
        # Load system prompt from the same file used by CLI
        try:
            with open("prompts/system_prompt.txt", "r", encoding="utf-8") as f:
                st.session_state.system_prompt_text = f.read()
        except Exception:
            st.session_state.system_prompt_text = "You are an AI Business Assistant for a small business."


def main():
    st.set_page_config(page_title="AI Business Assistant", page_icon="🤖", layout="centered")
    init_state()

    if not OPENAI_API_KEY:
        st.error("OPENAI_API_KEY not found. Create a .env file with OPENAI_API_KEY=...")
        st.stop()

    st.title("🤖 AI Business Assistant")
    st.caption("Role-based AI assistant for small businesses (portfolio MVP).")

    # Sidebar controls
    with st.sidebar:
        st.header("Settings")

        st.text_area(
            "Business context",
            key="business_context",
            height=180,
            placeholder="Paste products/services, hours, return policy, pricing rules, etc.",
            help="Tip: keep it short during development to reduce cost.",
        )

        st.selectbox(
            "Role",
            options=["sales", "support", "manager"],
            key="role",
            help="Changes assistant behavior: sales/support/manager",
        )

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Clear chat"):
                st.session_state.messages = []
        with col2:
            st.write("")

        st.divider()
        st.markdown("**Cost controls**")
        st.write(f"Model: `{MODEL_NAME}`")
        st.write(f"Max output tokens: `{MAX_OUTPUT_TOKENS}`")
        st.write(f"Temperature: `{TEMPERATURE}`")

    # Validate business context
    if not st.session_state.business_context.strip():
        st.info("Add a business context in the sidebar to start chatting.")
        st.stop()

    # Initialize LLM
    llm = ChatOpenAI(
        model=MODEL_NAME,
        api_key=OPENAI_API_KEY,
        temperature=TEMPERATURE,
        max_tokens=MAX_OUTPUT_TOKENS,
    )

    # Render chat history
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Chat input
    user_text = st.chat_input("Type a message...")
    if user_text:
        st.session_state.messages.append({"role": "user", "content": user_text})
        with st.chat_message("user"):
            st.markdown(user_text)

        system_text = build_system_message(
            business_context=st.session_state.business_context.strip(),
            role=st.session_state.role,
        )

        # Convert session chat to LangChain messages
        lc_messages = [SystemMessage(content=system_text)]
        for m in st.session_state.messages:
            if m["role"] == "user":
                lc_messages.append(HumanMessage(content=m["content"]))
            elif m["role"] == "assistant":
                lc_messages.append(AIMessage(content=m["content"]))

        # Call the model
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    resp = llm.invoke(lc_messages)
                    assistant_text = resp.content.strip()
                except Exception as e:
                    assistant_text = f"ERROR calling model: {e}"

                st.markdown(assistant_text)

        st.session_state.messages.append({"role": "assistant", "content": assistant_text})


if __name__ == "__main__":
    main()
