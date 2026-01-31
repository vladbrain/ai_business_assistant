````md
# 🤖 AI Business Assistant

AI Business Assistant is a role-based AI system designed to support **real business operations** such as sales, customer support, and management decision-making.

The goal of this project is not to build another generic chatbot, but to demonstrate how **LLMs can be used as constrained, cost-aware business tools** integrated into realistic workflows.

---

## ✨ Key features

* **Role-based behavior**: `sales`, `support`, `manager`
* Business-context–aware responses (policies, goals, constraints)
* Manager-focused outputs:
  * action plans
  * outbound call frameworks
  * coaching notes
* Designed to avoid hallucinated prices, promotions, or policies
* Cost-controlled LLM usage suitable for development
* Core **CLI application**
* Optional **Streamlit** web interface for demos and presentation

---

## 📂 Project structure

```text
ai_business_assistant/
├── app.py                  # CLI application (core logic)
├── ui_streamlit.py         # Streamlit UI
├── config.py               # Environment and model configuration
├── requirements.txt
├── README.md
│
├── prompts/
│   └── system_prompt.txt   # Constrained system prompt
│
├── memory/
│   └── history.json        # Local conversation memory (gitignored)
│
└── .gitignore
````

---

## 🚀 Run the app locally

### 1) Create and activate a virtual environment

**Windows**

```bat
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

---

### 2) Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3) Environment configuration

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=YOUR_API_KEY
MODEL_NAME=gpt-4o-mini
MAX_TURNS_TO_KEEP=8
MAX_OUTPUT_TOKENS=250
TEMPERATURE=0.2
```

---

### 4) Run CLI version

```bash
python app.py
```

---

### 5) Run Streamlit UI

```bash
streamlit run ui_streamlit.py
```

---

## 🔄 End-to-end flow

```text
Business Context
      ↓
Role Selection (manager / sales / support)
      ↓
Constrained LLM Execution
      ↓
Actionable Business Output
```

---

## 🧠 Example use case (Retail Manager)

**Scenario:**
January sales slowdown in a retail store with reduced foot traffic.

**Manager request:**

```
Create an action plan to improve outbound call quality during a slow sales period.
```

**Assistant output:**

* structured action plan
* outbound call framework focused on value and discovery
* coaching notes for evaluating call quality

---

## 🧩 What this project demonstrates

* How to treat LLMs as **business tools**, not chatbots
* How to constrain model behavior using context and roles
* How to design AI systems with cost awareness
* How to generate realistic, operational outputs
* How to separate:

  * business logic
  * prompt design
  * interface layer (CLI / UI)
* How to build an AI automation project suitable for production thinking

---

## 🚧 Future improvements

* CLI commands (`/role`, `/context`, `/clear`)
* Document-based context using RAG
* Multiple business profiles
* CRM / call-system integrations
* Authentication and access control
* Deployment-ready service layer

---

## ⚠️ Notes

* This is not a generic chatbot
* The assistant intentionally refuses to invent missing business data
* Output quality depends on the provided business context
* Designed for internal tooling and decision support

---

## 👤 Author  

**Vladimir Amzaiants**  
GitHub: **@vladbrain**  
On a mission to become a **ML / AI engineer pro** 💪

```
```