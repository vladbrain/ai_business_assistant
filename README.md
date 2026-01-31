```md
# AI Business Assistant

A role-based AI assistant for small businesses that demonstrates how Large Language Models (LLMs) can be embedded into real operational workflows with clear constraints and business logic.

This project is designed as a portfolio-ready MVP for AI Automation / AI Developer / AI Engineer roles.

---

## Business Problem

Small retail businesses often face:
- seasonal sales slowdowns
- inconsistent outbound sales calls
- limited time for managers to coach sales representatives
- generic scripts that do not reflect real store operations

Managers need a way to quickly generate consistent, high-quality sales and operational guidance without relying on rigid templates or ad-hoc advice.

---

## Solution

This project provides a lightweight AI assistant that:
- operates within a defined business context
- adapts behavior based on role (sales, support, manager)
- focuses on practical, realistic outputs rather than generic advice
- can be used for internal coaching, planning, and process improvement

The assistant is intentionally constrained to avoid hallucinated promotions, prices, or policies.

---

## Target Users

- Small retail business managers
- Sales team leaders
- Customer support supervisors
- Startups building internal AI tools
- AI automation and AI engineering teams (portfolio use)

---

## Key Features

- Role-based behavior: `sales`, `support`, `manager`
- Business-context–aware responses
- Manager-focused outputs such as action plans and coaching notes
- Outbound call frameworks and scripts focused on quality
- Cost-controlled LLM usage suitable for development and testing
- CLI-based core logic
- Optional Streamlit web interface for demo and presentation

---

## Tech Stack

- Python
- OpenAI API
- LangChain
- Streamlit (optional UI)
- JSON-based local storage
- Environment-based configuration (`.env`)

---

## Project Structure

```

ai_business_assistant/
├── app.py                  # CLI application (core logic)
├── ui_streamlit.py         # Optional Streamlit web interface
├── config.py
├── requirements.txt
├── README.md
├── prompts/
│   └── system_prompt.txt
├── memory/
│   └── history.json
└── .gitignore

````

---

## Example Use Case (Retail Manager)

**Scenario:**  
January sales slowdown in a Verizon retail store with a need to improve outbound call quality.

The assistant can:
- generate a clear action plan for outbound calling
- create realistic call scripts focused on value and discovery
- provide coaching notes for managers to evaluate call quality
- avoid referencing unconfirmed promotions or pricing

---

## Setup (Windows / VS Code)

### 1. Create and activate virtual environment
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
````

### 2. Install dependencies

```powershell
pip install -r requirements.txt
```

### 3. Create `.env` file

```env
OPENAI_API_KEY=YOUR_API_KEY
MODEL_NAME=gpt-4o-mini
MAX_TURNS_TO_KEEP=8
MAX_OUTPUT_TOKENS=250
TEMPERATURE=0.2
```

> `.env` is excluded from version control.

---

## Run (CLI)

```powershell
python app.py
```

---

## Run (Streamlit UI)

```powershell
streamlit run ui_streamlit.py
```

---

## Cost Control Strategy

This project is designed to minimize API usage during development:

* short conversation history
* capped response length
* low temperature for concise output
* focused system prompts

These patterns reflect real-world production constraints.

---

## Design Principles

* LLMs are treated as constrained tools, not general chatbots
* Business context is the single source of truth
* Quality and consistency are prioritized over verbosity
* The system is built to be extended, not over-engineered

---

## Future Improvements

* CLI commands for role and context switching
* Document-based context using RAG
* CRM or call system integrations
* Multi-store configuration
* Authentication and access control

---

## Disclaimer

This project is intended for educational and portfolio purposes only.
No real customer data should be used.

---

Vladimir Amzaiants
GitHub: @vladbrain
On a mission to become a ML / AI engineer pro 💪

```
```
