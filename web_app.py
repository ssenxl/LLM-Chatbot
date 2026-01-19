from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import os

from feedback_logger import log_feedback

from rag_engine import ask_it

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

class AskRequest(BaseModel):
    text: str

class FeedbackRequest(BaseModel):
    feedback: str

@app.get("/")
def root():
    return {"status": "ok"}

@app.get("/ui")
def ui():
    return FileResponse(os.path.join(STATIC_DIR, "index.html"))

@app.post("/ask")
def ask(req: AskRequest):
    return {"answer": ask_it(req.text)}

# เพิ่ม endpoint สำหรับรับ feedback
@app.post("/feedback")
async def feedback(req: FeedbackRequest):
    log_feedback(req.feedback)
    return {"status": "ok"}
#uvicorn web_app:app --reload --port 8000
#http://127.0.0.1:8000/static/index.html