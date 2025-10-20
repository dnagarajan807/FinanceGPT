import pandas as pd
from langchain_text_splitters import RecursiveCharacterTextSplitter

def load_financial_data(file_path: str):
    """
    Load financial CSV data and convert it into descriptive text summaries.

    Args:
        file_path (str): Path to the financial dataset CSV file.
    Returns:
        List[str]: List of textual summaries representing each row.
    """
    df = pd.read_csv(file_path)

    text_data = []
    for _, row in df.iterrows():
        text_data.append(
            f"In {row['Year']} Q{row['Quarter']}, revenue was {row['Revenue']} million, "
            f"OPEX was {row['OPEX']} million, and profit was {row['Profit']} million "
            f"for business unit {row['BusinessUnit']}."
        )
    return text_data


def chunk_texts(texts, chunk_size: int = 500, chunk_overlap: int = 100):
    """
    Split the given texts into smaller chunks for embedding and retrieval.

    Args:
        texts (List[str]): List of long text strings.
        chunk_size (int): Maximum characters per chunk.
        chunk_overlap (int): Overlap between chunks.
    Returns:
        List[Document]: List of LangChain Document objects.
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    docs = splitter.create_documents(texts)
    return docs
