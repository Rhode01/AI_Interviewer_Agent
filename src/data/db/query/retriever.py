from src.data.db.utils.embedding_ops import search_embeddings
from langchain_core.documents import Document
from src.data.db.base import AsyncSessionLocal

class PostgresRetriever:
    def __init__(self, label: str, k: int = 5):
        self.label = label
        self.k = k

    async def get_relevant_documents(self, query: str):
        async with AsyncSessionLocal() as session:
            results = await search_embeddings(session, query, self.label, self.k)
            return [Document(page_content=r.content, metadata={"label": r.label}) for r in results]
