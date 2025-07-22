# 🧠 DataTalk-E-Com-Q-A-Agent

This project builds an AI-powered agent that answers natural language questions based on product-level e-commerce data using a local SQL database and FastAPI.

---

## 🚀 Features

- Ask questions like “What is my total sales?” or “Which product had the highest CPC?”
- Converts natural questions into SQL queries using LLM logic
- Retrieves answers from structured SQLite data
- Frontend with a text box to ask questions (HTML + JS)
- Optionally visualizes results (bonus extension)

---

## 📂 Project Structure
genai_ecom_project/
│
├── main.py # FastAPI app with /ask and / route
├── db_setup.py # Converts CSVs into SQLite tables
├── query_executor.py # Runs SQL queries
├── llm_handler.py # Converts question → SQL (mock logic or LLM)
├── frontend.html # Simple web interface
├── requirements.txt # Dependencies
└── datasets/ # Put your 3 CSVs here
├── Ad_Sales.csv
├── Total_Sales.csv
└── Eligibility.csv

---

## ⚙️ How to Run

### 1. Install dependencies
pip install --user -r requirements.txt

2. Load datasets into SQLite DB
python db_setup.py

4. Start FastAPI server
python -m uvicorn main:app --reload

6. Open frontend
Option A: Visit http://127.0.0.1:8000 (served by FastAPI)
Option B: Open frontend.html manually in your browser
---

