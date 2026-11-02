import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
DATABASE = os.path.join(BASE_DIR, "storage.db")
SECRET_KEY = os.environ.get("SECRET_KEY", "change-this-secret-key")
MAX_CONTENT_LENGTH = 50 * 1024 * 1024  # 50 MB per upload

ALLOWED_EXTENSIONS = {
    "txt", "pdf", "png", "jpg", "jpeg", "gif", "doc", "docx",
    "xls", "xlsx", "ppt", "pptx", "csv", "zip", "mp3", "mp4",
}
