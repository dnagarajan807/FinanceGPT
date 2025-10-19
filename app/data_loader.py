import pandas as pd
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_financial_data(file_path: str):
    df = pd.read_csv(file_path)
    # Convert numeric columns to text summaries
    text_data = []
    for _, row in df.iterrows():
        text_data.append(
            f"In {row['Year']} Q{row['Quarter']}, revenue was {row['Revenue']} million, "
            f"OPEX was {row['OPEX']} million, and profit was {row['Profit']} million "
            f"for business unit {row['BusinessUnit']}."
        )
    return text_data

def chunk_texts(texts):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    docs = splitter.create_documents(texts)
    return docs
