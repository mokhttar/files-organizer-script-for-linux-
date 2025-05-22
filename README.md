File Organizer Script
A simple Python script that organizes files in a directory by their extensions (Linux only).

Features
Automatically creates folders for each file extension

Moves files into their corresponding extension folders

Handles files with spaces in names

Skips files without extensions

Works with complex extensions (like .tar.gz)

Requirements
Python 3.x

Linux system

Installation
No installation needed. Just download the script:

bash
wget https://example.com/file_organizer.py
chmod +x file_organizer.py
Usage
bash
python3 file_organizer.py
When prompted, enter the directory path or press Enter to use current directory.

Examples
Organize current directory:

bash
$ python3 file_organizer.py
The script is running on linux
Please provide the path to your directory. If not specified, the script's current directory will be used by default

/home/user/Documents
Creating folder: pdf
Moving file1.pdf to pdf/
Creating folder: jpg
Moving photo.jpg to jpg/
Organize specific directory:

bash
$ python3 file_organizer.py
The script is running on linux
Please provide the path to your directory. If not specified, the script's current directory will be used by default
/home/user/Downloads
Sample directory before:

downloads/
├── document.pdf
├── image.jpg
├── archive.tar.gz
└── notes.txt
After running script:

downloads/
├── pdf/
│   └── document.pdf
├── jpg/
│   └── image.jpg
├── gz/
│   └── archive.tar.gz
└── txt/
    └── notes.txt
Notes
The script will skip files without extensions

For files with multiple extensions (like .tar.gz), only the last extension (.gz) will be used

Requires Linux system (won't work on Windows/Mac)

License
This is free and unencumbered software released into the public domain.
