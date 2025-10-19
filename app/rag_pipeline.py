from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from app.vector_store import create_or_load_vector_store
from app.data_loader import load_financial_data, chunk_texts
from app.config import Config

def build_rag_pipeline():
    texts = load_financial_data(Config.DATA_PATH)
    docs = chunk_texts(texts)
    vector_store = create_or_load_vector_store(docs)

    llm = ChatOpenAI(model=Config.LLM_MODEL, temperature=0, openai_api_key=Config.OPENAI_API_KEY)
    retriever = vector_store.as_retriever(search_kwargs={"k": 3})

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )
    return qa_chain

def query_financegpt(question: str):
    qa = build_rag_pipeline()
    response = qa(question)
    return {
        "answer": response["result"],
        "sources": [doc.metadata for doc in response["source_documents"]]
    }
