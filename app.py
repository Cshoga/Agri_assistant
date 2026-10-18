from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from datasets import load_dataset
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the agriculture Q&A dataset and index the questions
try:
    ds = load_dataset("KisanVaani/agriculture-qa-english-only")["train"]
    questions = ds["question"]
    answers = ds["answers"]
    vectorizer = TfidfVectorizer(ngram_range=(1, 2), stop_words="english")
    q_matrix = vectorizer.fit_transform(questions)
except Exception as e:
    raise RuntimeError(f"Failed to load the dataset: {str(e)}")

class ChatRequest(BaseModel):
    user_input: str
    context: str = ""  # kept so existing requests still validate; not used

def chatbot_response(user_input: str) -> str:
    scores = cosine_similarity(vectorizer.transform([user_input]), q_matrix)[0]
    best = int(scores.argmax())
    if scores[best] < 0.15:
        return "Sorry, I couldn't find a good answer. Try rephrasing your farming question."
    return answers[best]

@app.post("/chat")
def chat(request: ChatRequest):
    try:
        return {"response": chatbot_response(request.user_input)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Run with: python -m uvicorn app:app --port 8000 --reload
