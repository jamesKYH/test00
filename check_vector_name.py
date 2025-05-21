import sys
import os
from mcp_server_qdrant.embeddings.fastembed import FastEmbedProvider
from mcp_server_qdrant.settings import EmbeddingProviderSettings

# 기본 설정을 사용하여 벡터 이름 확인
settings = EmbeddingProviderSettings()
provider = FastEmbedProvider(settings.model_name, vector_name=settings.vector_name)
print(f"벡터 이름: {provider.get_vector_name()}")

# (vector_name=None 파라미터로 확인)
provider_no_name = FastEmbedProvider(settings.model_name, vector_name=None)
print(f"vector_name=None인 경우 벡터 이름: {provider_no_name.get_vector_name()}")

# 직접 변수를 설정하여 확인
os.environ["VECTOR_NAME"] = "all-MiniLM-L6-v2"
provider_env = FastEmbedProvider(settings.model_name)
print(f"환경 변수 설정 후 벡터 이름: {provider_env.get_vector_name()}")

print("\n모듈 경로:")
print(f"FastEmbedProvider: {FastEmbedProvider.__module__}")
print(f"EmbeddingProviderSettings: {EmbeddingProviderSettings.__module__}") 