from fastapi import FastAPI
from RAG_CHATBOT.chat import router as chat_router
from fastapi.staticfiles import StaticFiles


app = FastAPI()


app.include_router(chat_router, prefix="/api")


app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def home():
    return {"message": "Chatbot API Çalışıyor!"}
