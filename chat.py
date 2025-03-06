from fastapi import APIRouter, Form
from RAG_CHATBOT.pine_cone import query_pinecone

router = APIRouter()

@router.post("/chat")
def chat(query: str = Form(...)):
    """
    HTML formdan gelen POST isteğini alıp Pinecone veritabanında sorgulayıp yanıt döndürür.
    """
    results = query_pinecone(query)
    return {"query": query, "results": results}