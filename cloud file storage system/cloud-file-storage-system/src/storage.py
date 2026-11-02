import os
from datetime import datetime
from werkzeug.utils import secure_filename
from src.config import UPLOAD_FOLDER, ALLOWED_EXTENSIONS


def user_folder(user_id):
    """Each user gets a private folder: uploads/user_<id>/"""
    path = os.path.join(UPLOAD_FOLDER, f"user_{user_id}")
    os.makedirs(path, exist_ok=True)
    return path


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def save_file(user_id, file):
    """Saves an uploaded file. Returns the saved filename or None if invalid."""
    if not file or file.filename == "" or not allowed_file(file.filename):
        return None

    filename = secure_filename(file.filename)
    folder = user_folder(user_id)

    # Avoid overwriting: report.pdf -> report_1.pdf
    name, ext = os.path.splitext(filename)
    counter = 1
    while os.path.exists(os.path.join(folder, filename)):
        filename = f"{name}_{counter}{ext}"
        counter += 1

    file.save(os.path.join(folder, filename))
    return filename


def format_size(size):
    for unit in ("B", "KB", "MB", "GB"):
        if size < 1024:
            return f"{size:.0f} {unit}" if unit == "B" else f"{size:.1f} {unit}"
        size /= 1024
    return f"{size:.1f} TB"


def list_files(user_id):
    folder = user_folder(user_id)
    files = []
    for name in os.listdir(folder):
        path = os.path.join(folder, name)
        if os.path.isfile(path):
            info = os.stat(path)
            files.append(
                {
                    "name": name,
                    "size": format_size(info.st_size),
                    "modified": datetime.fromtimestamp(info.st_mtime).strftime("%d %b %Y, %H:%M"),
                    "mtime": info.st_mtime,
                }
            )
    return sorted(files, key=lambda f: f["mtime"], reverse=True)


def delete_file(user_id, filename):
    path = os.path.join(user_folder(user_id), secure_filename(filename))
    if os.path.isfile(path):
        os.remove(path)
        return True
    return False
