#  Duplicate File Remover

A Python utility to detect and delete duplicate files based on content using MD5 hashing.

##  Features
- Scans files in a folder (ignores subfolders)
- Detects duplicates using content (not filename)
- Asks before deleting duplicates
- Deletes only the duplicates, keeps original

##  How to Use
1. Add your test `.txt` files in a folder (e.g., `test_files`)
2. Set `folder = "test_files"` in the Python script
3. Run the script with Python 3
4. Follow the prompts to delete duplicates

## Technologies
- Python 3.11
- Modules: `os`, `hashlib`

## What I Learned
- File handling and hashing in Python
- Detecting duplicate content
- Writing safe delete logic

## Future Ideas
- GUI version (Tkinter)
- Safe delete using Recycle Bin
- Recursive folder support
 
## Notes
- Works only on files (not subfolders)
- Deletion is optional and confirmed before execution
