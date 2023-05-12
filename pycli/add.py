from qdrant_client import QdrantClient
import numpy as np
from qdrant_client.models import PointStruct

# client = QdrantClient(host="localhost", port=6333)
# client = QdrantClient(url="http://localhost:6333")
# 支持 GRPC
client = QdrantClient(host="localhost", grpc_port=6334, prefer_grpc=True)

# 随机插入 100 条 100维 的向量
vectors = np.random.rand(100, 100)
client.upsert(
    collection_name="my_collection",
    points=[
        PointStruct(
            id=idx,
            vector=vector.tolist(),
            payload={"color": "red", "rand_number": idx % 10}
        )
        for idx, vector in enumerate(vectors)
    ]
)