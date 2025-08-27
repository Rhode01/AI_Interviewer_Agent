from sqlalchemy import select,func
from src.data.db.models.schema import DocumentEmbedding
from src.model.embedding import embeddings
async def search_embeddings(session, query: str, label: str, k: int = 5):
    query_vec = embeddings.embed_query(query)
    stmt = (
        select(DocumentEmbedding)
        .where(DocumentEmbedding.label == label)
        .order_by(DocumentEmbedding.embedding.cosine_distance(query_vec))
        .limit(k)
    )
    results = await session.execute(stmt)
    return results.scalars().all()
async def label_exists(session, label: str) -> bool:
    stmt = select(func.count()).select_from(DocumentEmbedding).where(DocumentEmbedding.label == label)
    result = await session.execute(stmt)
    return result.scalar() > 0
