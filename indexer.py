import json
from reader import read_file

def create_index(files, output_file="index/index.json"):
    index = []
    for file in files:
        content = read_file(file)
        if content:
            index.append({
                "file_path": file,
                "content": content
            })
    
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False, indent=4)
    print(f"Index créé et sauvegardé dans {output_file}")
