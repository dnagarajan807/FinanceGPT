from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from langchain_openai import ChatOpenAI
from app.vector_store import create_or_load_vector_store
from app.data_loader import load_financial_data, chunk_texts
from app.config import Config


def build_rag_pipeline():
    # 1. Load and chunk data
    texts = load_financial_data(Config.DATA_PATH)
    docs = chunk_texts(texts)

    # 2. Create or load vector store
    vector_store = create_or_load_vector_store(docs)

    # 3. Create retriever
    retriever = vector_store.as_retriever(search_kwargs={"k": 3})

    # 4. Define LLM
    llm = ChatOpenAI(
        model=Config.LLM_MODEL,
        temperature=0,
        api_key=Config.OPENAI_API_KEY,
    )

    # 5. Create prompt template
    prompt = ChatPromptTemplate.from_template(
        """You are a financial assistant. Use the following context to answer the question.

        Context:
        {context}

        Question:
        {question}

        Provide a concise and accurate answer."""
    )

    # 6. Build the chain using Runnable interfaces
    rag_chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
    )

    return rag_chain


def query_financegpt(question: str):
    rag_chain = build_rag_pipeline()
    response = rag_chain.invoke(question)
    return {"answer": response.content}
