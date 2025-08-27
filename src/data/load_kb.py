from pathlib import Path
import sys
from langchain_community.document_loaders.text import TextLoader
from langchain_community.document_loaders.pdf import PyPDFLoader
from langchain_experimental.text_splitter import SemanticChunker
from pathlib import Path
from src.model.embedding import embeddings
from src.data.db.models.schema import DocumentEmbedding
from src.data.db.query.retriever import PostgresRetriever
from src.data.db.utils.embedding_ops import label_exists
from src.data.db.base import AsyncSessionLocal

async def store_embeddings_toDb(session, docs, label: str):
    db_objs = []
    for doc in docs:
        vector = embeddings.embed_query(doc.page_content)
        db_objs.append(
            DocumentEmbedding(
                label=label,
                content=doc.page_content,
                embedding=vector
            )
        )
    session.add_all(db_objs)
    await session.commit()


async def load_kb(label: str):
    async with AsyncSessionLocal() as session:
        if await label_exists(session, label):
            print(f"[INFO] Knowledge base for '{label}' already exists. Using existing embeddings.")
            return PostgresRetriever(label=label, k=5)
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
        chuck_docs = chucker.split_documents(docs)
        
        await store_embeddings_toDb(session, chuck_docs, label)
        return PostgresRetriever(label=label, k=5)


