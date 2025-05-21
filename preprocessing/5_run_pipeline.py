# 📁 preprocessing/run_pipeline.py
import subprocess
import os
from pathlib import Path

# 실행할 파이프라인 스크립트 목록
scripts = [
    "1_load_text.py",
    "2_split_chunks.py",
    "3_embed_chunks.py",
    "4_upload_qdrant.py"
]

# 각 스크립트 순차적으로 실행
for script in scripts:
    print(f"\n▶ 실행: {script}")
    try:
        subprocess.run(["python", script], check=True)
    except Exception as e:
        print(f"❌ 오류 발생: {e}")

print("\n✅ 전체 파이프라인 완료")