from qdrant_client import QdrantClient
import json

# Qdrant 서버에 연결
client = QdrantClient(host="localhost", port=6333)
COLLECTION_NAME = "my-collection"

# 컬렉션이 존재하는지 확인
if not client.collection_exists(COLLECTION_NAME):
    print(f"❌ 컬렉션 '{COLLECTION_NAME}'가 존재하지 않습니다!")
    exit(1)

# 컬렉션 정보 확인
collection_info = client.get_collection(COLLECTION_NAME)
print(f"✅ 컬렉션 정보:")
print(f"   - 벡터 설정: {collection_info.config.params.vectors}")
print(f"   - 포인트 수: {collection_info.vectors_count}")

# 샘플 데이터 확인
print("\n✅ 처음 10개 데이터 샘플:")
points = client.scroll(
    collection_name=COLLECTION_NAME,
    limit=10,
    with_payload=True,
    with_vectors=False
)[0]

for i, point in enumerate(points):
    print(f"\n데이터 {i+1}:")
    print(f"ID: {point.id}")
    print(f"페이로드 키: {list(point.payload.keys())}")
    
    # 처음 한 개만 자세히 출력
    if i == 0:
        print("\n첫 번째 데이터 상세:")
        for key, value in point.payload.items():
            print(f"  - {key}: {str(value)[:100]}{'...' if len(str(value)) > 100 else ''}") 