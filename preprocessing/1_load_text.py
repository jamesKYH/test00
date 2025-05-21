# 📁 preprocessing/1_load_text.py
from pathlib import Path

RAW_DIR = Path("../data/raw")
# 모든 텍스트 파일을 하나로 합칩니다
OUTPUT_FILE = Path("../data/intermediate/raw_text.txt")

def load_text():
    output_dir = OUTPUT_FILE.parent
    output_dir.mkdir(parents=True, exist_ok=True)
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as out_file:
        for file_path in RAW_DIR.glob('*.txt'):
            with open(file_path, 'r', encoding='utf-8') as input_file:
                out_file.write(input_file.read() + "\n\n")
    
    print(f"✅ 텍스트 로드 완료: {OUTPUT_FILE}")

if __name__ == "__main__":
    load_text()