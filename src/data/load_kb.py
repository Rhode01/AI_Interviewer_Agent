from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders.text import TextLoader
from langchain_community.document_loaders.pdf import PyPDFLoader
from langchain_experimental.text_splitter import SemanticChunker
from pathlib import Path
from src.model.embedding import embeddings

def load_kb():
    docs_path = Path(__file__).resolve().parents[0] / "knowledge_base"
    docs = []

    for file in docs_path.glob("*.txt"):
        loader = TextLoader(str(file))
        docs.extend(loader.load())
    for file in docs_path.glob("*.pdf"):
        loader = PyPDFLoader(str(file))
        docs.extend(loader.load())
    chucker = SemanticChunker(
        embeddings, 
        breakpoint_threshold_type="percentile",
        breakpoint_threshold_amount=95,
        min_chunk_size=800
    )
    chuck_docs = chucker.split_documents(doc for doc in docs)

    vectore_store =  FAISS.from_documents(chuck_docs,embeddings)
    retriever = vectore_store.as_retriever()
    return retriever
    

