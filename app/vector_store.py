import os
from langchain_community.vectorstores import FAISS
from langchain_openai.embeddings import OpenAIEmbeddings
from app.config import Config

def create_or_load_vector_store(docs):
    embeddings = OpenAIEmbeddings(model=Config.EMBEDDING_MODEL, openai_api_key=Config.OPENAI_API_KEY)
    if os.path.exists(Config.VECTOR_STORE_PATH):
        return FAISS.load_local(Config.VECTOR_STORE_PATH, embeddings, allow_dangerous_deserialization=True)
    else:
        db = FAISS.from_documents(docs, embeddings)
        db.save_local(Config.VECTOR_STORE_PATH)
        return db
