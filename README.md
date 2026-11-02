# Cloud File Storage System

A web-based cloud storage application built with **Python (Flask)**. Users can register, log in, and securely upload, download, and delete their own files. Every user gets a private storage folder.

## Features
- User registration and login (passwords stored as secure hashes)
- Upload files (allowed file types only, 50 MB limit)
- Download and delete files
- Private folder for each user
- Automatic handling of duplicate file names (`report.pdf` becomes `report_1.pdf`)

## Tech Stack
- **Language:** Python 3
- **Framework:** Flask
- **Database:** SQLite (user accounts)
- **Frontend:** HTML, CSS (Jinja2 templates)

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
├── requirements.txt     # dependencies
└── README.md
```

## How to Run

1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/cloud-file-storage-system.git
cd cloud-file-storage-system
```

2. (Optional) Create a virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run the application
```bash
python app.py
```

5. Open **http://127.0.0.1:5000** in your browser, register an account, and start uploading files.

## Usage
1. Register a new account
2. Log in with your username and password
3. Upload files from the dashboard
4. Download or delete your files anytime

## Author
**Your Name**
GitHub: [YOUR_USERNAME](https://github.com/YOUR_USERNAME)
