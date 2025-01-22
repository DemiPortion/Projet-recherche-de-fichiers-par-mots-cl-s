import os

def scan_folder(folder_path, supported_extensions=[".txt", ".pdf", ".docx"]):
    files = []
    for root, dirs, filenames in os.walk(folder_path):
        for filename in filenames:
            if any(filename.endswith(ext) for ext in supported_extensions):
                files.append(os.path.join(root, filename))
    return files
