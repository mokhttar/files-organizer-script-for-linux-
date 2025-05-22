# File Organizer Script

A simple Python script that organizes files in a directory by their extensions (Linux only).

## Features
- Automatically creates folders for each file extension
- Moves files into their corresponding extension folders
- Handles files with spaces in names
- Skips files without extensions
- Works with complex extensions (like .tar.gz)

## Requirements
- Python 3.x
- Linux system

## Installation
```bash
wget https://raw.githubusercontent.com/yourusername/file_organizer/main/file_organizer.py
chmod +x file_organizer.py
```

## Usage
```bash
python3 file_organizer.py
```

When prompted, enter the directory path or press Enter to use current directory.

## Examples

### 1. Organize current directory
```bash
$ python3 file_organizer.py
The script is running on linux
Please provide the path to your directory...
[Press Enter]
/home/user/Documents
Creating folder: pdf
Moving report.pdf to pdf/
Creating folder: jpg
Moving photo.jpg to jpg/
```

### 2. Organize specific directory
```bash
$ python3 file_organizer.py
The script is running on linux
Please provide the path to your directory...
/home/user/Downloads
```

### 3. Directory structure before:
```
downloads/
├── document.pdf
├── image.jpg
├── data.csv
└── notes.txt
```

After running:
```
downloads/
├── pdf/
│   └── document.pdf
├── jpg/
│   └── image.jpg
├── csv/
│   └── data.csv
└── txt/
    └── notes.txt
```

## Notes
- Files without extensions will be skipped
- For files like "archive.tar.gz", they'll go in "gz/" folder
- Requires Linux (tested on Ubuntu/Debian)

## Troubleshooting
If you get permission errors:
```bash
chmod +x file_organizer.py
```

For Python errors:
```bash
python3 -m pip install --upgrade pip
```

---

*"Works great for organizing messy downloads folders!" - Happy User(Ad3iwlna blkhayr)*
