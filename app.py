from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import tensorflow as tf
from transformers import TFAutoModelForCausalLM, AutoTokenizer
from fastapi.middleware.cors import CORSMiddleware


# Initialize FastAPI app
app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the saved model and tokenizer
try:
    loaded_model = TFAutoModelForCausalLM.from_pretrained("chatbot")
    loaded_tokenizer = AutoTokenizer.from_pretrained("chatbot")
except Exception as e:
    raise RuntimeError(f"Failed to load the model or tokenizer: {str(e)}")

# Define request model
class ChatRequest(BaseModel):
    user_input: str
    context: str = "Agriculture-related information goes here"

# Define chatbot response function
def chatbot_response(user_input: str, context: str):
    input_text = f"{context}\n\nUser: {user_input}\n\nChatbot:"
    inputs = loaded_tokenizer(input_text, return_tensors="tf")
    
    output_sequences = loaded_model.generate(
        input_ids=inputs["input_ids"],
        max_length=100,
        temperature=0.7,
        top_k=50,
        top_p=0.9,
        do_sample=True
    )
    
    response = loaded_tokenizer.decode(output_sequences[0], skip_special_tokens=True)
    response = response.split("Chatbot:")[-1].strip()
    
    return response

# API endpoint to get chatbot response
@app.post("/chat")
def chat(request: ChatRequest):
    try:
        response = chatbot_response(request.user_input, request.context)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Run the FastAPI app using: uvicorn app:app --reload
