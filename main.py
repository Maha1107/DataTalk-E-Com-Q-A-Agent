from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from pydantic import BaseModel
from llm_handler import convert_question_to_sql
from query_executor import execute_sql_query
import os

app = FastAPI()

class QuestionRequest(BaseModel):
    question: str

@app.post("/ask")
async def ask(request: QuestionRequest):
    question = request.question
    sql_query = convert_question_to_sql(question)
    result = execute_sql_query(sql_query)
    return {
        "question": question,
        "sql_query": sql_query,
        "result": result
    }

# ✅ Add this route to serve the HTML page
@app.get("/", response_class=HTMLResponse)
async def get_frontend():
    return FileResponse(os.path.join("frontend.html"))
