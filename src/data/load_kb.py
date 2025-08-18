from pathlib import Path
import sys
project_folder = Path(__file__).resolve().parents[2]
sys.path.append(str(project_folder))
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders.text import TextLoader
from langchain_community.document_loaders.pdf import PyPDFLoader
from langchain_experimental.text_splitter import SemanticChunker
from pathlib import Path
from src.model.embedding import embeddings

def load_kb():
    docs_path = Path(__file__).resolve().parents[1] / "data" / "knowledge_base"
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
    page_content = [doc.page_content for doc in docs]
    chuck_docs = chucker.split_documents(docs)
    print(len(chuck_docs))
    print(chuck_docs)
    vectore_store =  FAISS.from_documents(chuck_docs,embeddings)
    retriever = vectore_store.as_retriever()
    return retriever
    