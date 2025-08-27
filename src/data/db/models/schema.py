from sqlalchemy import Column, Integer, String,Text
from pgvector.sqlalchemy import Vector
from src.data.db.base import Base

class DocumentEmbedding(Base):
    __tablename__ = "document_embeddings"
    __table_args__ = {"extend_existing": True}
    id = Column(Integer, primary_key=True, index=True)
    label =Column(Text, nullable=False)
    content = Column(String, nullable=False)   
    embedding = Column(Vector(1536))