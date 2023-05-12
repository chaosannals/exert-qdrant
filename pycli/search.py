import asyncio
from qdrant_client import QdrantClient, grpc
import numpy as np
from qdrant_client.models import PointStruct,  Filter, FieldCondition, Range

# 支持 HTTP
# client = QdrantClient(host="localhost", port=6333)
# client = QdrantClient(url="http://localhost:6333")
# 支持 GRPC
client = QdrantClient(host="localhost", grpc_port=6334, prefer_grpc=True)

# 随机生成向量 查找最近
query_vector = np.random.rand(100)
hits = client.search(
    collection_name="my_collection",
    query_vector=query_vector,
    limit=5  # Return 5 closest points
)

print('====================================1')
for hit in hits:
    print(hit)

# 支持条件过滤
hits = client.search(
    collection_name="my_collection",
    query_vector=query_vector,
    query_filter=Filter(
        must=[  # 查询结果必须满足以下字段条件
            FieldCondition(
                key='rand_number',  # 指定 `rand_number` 字段附加条件.
                range=Range(
                    gte=3  # 要求 `rand_number` >= 3
                )
            )
        ]
    ),
    limit=4  # Return 5 closest points
)

print('====================================2')
for hit in hits:
    print(hit)


print('====================================3')

async def run_on_async():
    # 容器必须在同个 loop 里面被生成。要么自己获取loop ,要么干脆放一起。
    grpc_collections = client.async_grpc_collections

    res = await grpc_collections.List(
        grpc.ListCollectionsRequest(),
        timeout=1.0
    )
    print(res)

asyncio.run(run_on_async())