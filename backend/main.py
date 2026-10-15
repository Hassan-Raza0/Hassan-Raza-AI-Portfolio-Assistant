from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

BASE_DIR = Path(__file__).resolve().parent.parent
KNOWLEDGE_FILE = BASE_DIR / "knowledge" / "portfolio_info.txt"

app = FastAPI(
    title="Hassan Raza AI Portfolio Assistant",
    description="AI assistant for Hassan Raza's personal portfolio",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    question: str


def load_portfolio_info():
    if not KNOWLEDGE_FILE.exists():
        raise FileNotFoundError(f"{KNOWLEDGE_FILE} was not found")
    return KNOWLEDGE_FILE.read_text(encoding="utf-8")


@app.get("/")
def home():
    return {"message": "Hassan Raza AI Portfolio Assistant is running!"}
