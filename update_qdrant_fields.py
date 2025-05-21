from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct, VectorParams, Distance
import json

# Qdrant 클라이언트 초기화
client = QdrantClient(host="localhost", port=6333)
COLLECTION_NAME = "my-collection"

# 컬렉션이 존재하는지 확인
if not client.collection_exists(COLLECTION_NAME):
    print(f"❌ 컬렉션 '{COLLECTION_NAME}'가 존재하지 않습니다!")
    exit(1)

# 모든 포인트 가져오기
print(f"📊 '{COLLECTION_NAME}' 컬렉션에서 모든 포인트 조회 중...")
points = client.scroll(
    collection_name=COLLECTION_NAME,
    limit=10000,  # 충분히 큰 값으로 설정
    with_payload=True,
    with_vectors=True
)[0]

print(f"✅ 총 {len(points)}개 포인트를 읽었습니다.")

# 각 포인트를 업데이트하여 'content'를 'document'로 복사
updated_points = []
for point in points:
    # 'content' 필드가 있는지 확인
    if 'content' in point.payload:
        # 벡터 이름 확인
        vector_names = list(point.vector.keys()) if isinstance(point.vector, dict) else ["all-MiniLM-L6-v2"]
        
        # 포인트 업데이트 준비
        updated_point = PointStruct(
            id=point.id,
            vector=point.vector,
            payload={
                **point.payload,  # 기존 payload 유지
                "document": point.payload['content']  # 'content' 값을 'document'에 복사
            }
        )
        updated_points.append(updated_point)

if not updated_points:
    print("⚠️ 업데이트할 포인트가 없습니다.")
    exit(0)

# 업데이트된 포인트 저장
print(f"🔄 {len(updated_points)}개 포인트 업데이트 중...")
client.upsert(
    collection_name=COLLECTION_NAME,
    points=updated_points,
    wait=True
)

print(f"✅ 업데이트 완료! 모든 포인트에 'document' 필드가 추가되었습니다.") 