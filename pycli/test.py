from qdrant_client import QdrantClient

# 这东西允许不连服务器，使用 sqlite 做测试
client = QdrantClient(":memory:")
