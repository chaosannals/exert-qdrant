from qdrant_client import QdrantClient

from qdrant_client.models import Distance, VectorParams

client = QdrantClient(host="localhost", port=6333)
# client = QdrantClient(url="http://localhost:6333")

# 创建集合
client.recreate_collection(
    collection_name="my_collection",
    vectors_config=VectorParams(size=100, distance=Distance.COSINE),
)