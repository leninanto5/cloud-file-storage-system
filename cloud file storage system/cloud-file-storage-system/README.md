# Cloud File Storage System

A simple web-based cloud storage application built with **Python (Flask)**. Users can register, log in, and securely upload, download, and delete their own files. Every user gets a private storage folder.

## Features
- User registration and login (passwords stored as secure hashes)
- Upload files (type and size restricted, 50 MB limit)
- Download and delete files
- Private folder per user
- Duplicate filename handling (`report.pdf` -> `report_1.pdf`)

## Tech Stack
- Python 3, Flask
- SQLite (user accounts)
- HTML, CSS (Jinja2 templates)

## Project Structure
```
cloud-file-storage-system/
├── src/
│   ├── config.py        # settings
│   ├── database.py      # SQLite user accounts
│   ├── storage.py       # file save / list / delete logic
│   ├── templates/       # HTML pages
│   └── static/          # CSS
├── uploads/             # user files (created at runtime)
├── app.py               # application entry point
├── requirements.txt
└── README.md
```

## How to Run
```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/cloud-file-storage-system.git
cd cloud-file-storage-system

# 2. (Optional) create a virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Mac/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python app.py
```
Open **http://127.0.0.1:5000** in your browser, register an account, and start uploading.

## Author
Your Name
