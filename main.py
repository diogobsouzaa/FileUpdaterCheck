import os
import shutil

def get_file_sizes(folder):
    file_sizes = {}
    for root, _, files in os.walk(folder):
        for file in files:
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, folder)
            file_sizes[relative_path] = os.path.getsize(file_path)
    return file_sizes

def compare_and_copy(p1, p2, att):
    sizes_p1 = get_file_sizes(p1)
    sizes_p2 = get_file_sizes(p2)
    
    if not os.path.exists(att):
        os.makedirs(att)
    
    for file, size in sizes_p1.items():
        if file not in sizes_p2 or sizes_p2[file] != size:
            source_path = os.path.join(p1, file)
            dest_path = os.path.join(att, file)
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)
            shutil.copy2(source_path, dest_path)
            print(f'Arquivo atualizado: {file}')

# Exemplo de uso:
p1 = r"path1 (updated)"
p2 = r"path2 (old)"
p_att = r"modified files only folder"

compare_and_copy(p1, p2, p_att)
