import os
import hashlib
import zipfile

file_path = r"C:\Itransition\Task_02\task2.zip"
dir_path = r"C:\Itransition\Task_02\temp"
result = ""

def calculate_hash(file_path):
    hash_function = hashlib.sha3_256()
    with open(file_path, 'rb') as file:
        while True:
            chunk = file.read(4096)
            if not chunk:
                break
            hash_function.update(chunk)
    return hash_function.hexdigest().lower()

with zipfile.ZipFile(file_path, 'r') as zip_ref:
    zip_ref.extractall(dir_path)

hashes = []
for root, dirs, files in os.walk(dir_path):
    for file in files:
        file_path = os.path.join(root, file)
        hash_value = calculate_hash(file_path)
        hashes.append(hash_value)

sorted_hashes = sorted(hashes)
result = ''.join(sorted_hashes)
result += "muk74dir@gmail.com"
final_hash = hashlib.sha3_256(result.encode()).hexdigest().lower()
print(final_hash)
