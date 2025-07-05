import os
import hashlib

def hash_file(filepath):
    hasher = hashlib.md5()
    with open(filepath, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

def find_duplicates(folder_path):
    hashes = {}
    print("Scanning files in:", folder_path)
    for filename in os.listdir(folder_path):
        full_path = os.path.join(folder_path, filename)
        if os.path.isfile(full_path):
            file_hash = hash_file(full_path)
            print(f"{full_path} -> {file_hash}")
            if file_hash in hashes:
                hashes[file_hash].append(full_path)
            else:
                hashes[file_hash] = [full_path]
    return hashes

def delete_duplicates(duplicates_dict):
    for file_list in duplicates_dict.values():
        if len(file_list) > 1:
            print("\nDuplicate group:")
            for i, file_path in enumerate(file_list):
                print(f"{i+1}. {file_path}")
            choice = input("Do you want to delete all except the first file? (y/n): ").lower()
            if choice == 'y':
                for file_path in file_list[1:]:
                    try:
                        os.remove(file_path)
                        print(f"Deleted: {file_path}")
                    except Exception as e:
                        print(f"Failed to delete {file_path}: {e}")
            else:
                print("Skipped deletion for this group.")

# ===== Main Logic =====
folder = "test_files"
duplicates = find_duplicates(folder)
delete_duplicates(duplicates)
