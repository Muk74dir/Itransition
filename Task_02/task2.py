import os
import hashlib
import zipfile

file_path = r"C:\Users\User\OneDrive\Desktop\Itransition\task2.zip"
dir_path = r"C:\Users\User\OneDrive\Desktop\Itransition"

# Function to calculate SHA3-256 hash of a file
def calculate_hash(file_path):
    with open(file_path, 'rb') as f:
        data = f.read()
        print(data)
        return hashlib.sha3_256(data).hexdigest()

# Function to read all files from a directory recursively
def read_files_from_dir(dir_path):
    file_list = []
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list

# Extract files from the ZIP archive
with zipfile.ZipFile('task2.zip', 'r') as zip_ref:
    zip_ref.extractall('temp')

# Read all files from the extracted directory
files = read_files_from_dir('temp')

# Calculate SHA3-256 hashes for each file
hashes = [calculate_hash(file) for file in files]
print(hashes)

# Sort the hashes in ascending order
sorted_hashes = sorted(hashes)

# Join sorted hashes without any separator
joined_hashes = ''.join(sorted_hashes)

# Concatenate the sorted hashes with your email in lowercase
result_string = joined_hashes + 'your.email@example.com'

# Calculate the SHA3-256 hash of the result string
final_hash = hashlib.sha3_256(result_string.encode()).hexdigest()

print(final_hash)
