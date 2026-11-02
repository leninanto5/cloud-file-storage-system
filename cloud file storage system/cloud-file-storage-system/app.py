from functools import wraps

from flask import (
    Flask, render_template, request, redirect,
    url_for, session, flash, send_from_directory,
)
from werkzeug.utils import secure_filename

from src import config
from src.database import init_db, create_user, verify_user
from src.storage import user_folder, save_file, list_files, delete_file

app = Flask(
    __name__,
    template_folder="src/templates",
    static_folder="src/static",
)
app.config["SECRET_KEY"] = config.SECRET_KEY
app.config["MAX_CONTENT_LENGTH"] = config.MAX_CONTENT_LENGTH

init_db()


def login_required(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        if "user_id" not in session:
            return redirect(url_for("login"))
        return view(*args, **kwargs)
    return wrapped


@app.route("/")
def home():
    return redirect(url_for("dashboard" if "user_id" in session else "login"))


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")
        if len(username) < 3 or len(password) < 6:
            flash("Username needs 3+ characters and password 6+ characters.", "error")
        elif create_user(username, password):
            flash("Account created. Please log in.", "success")
            return redirect(url_for("login"))
        else:
            flash("That username is already taken.", "error")
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = verify_user(
            request.form.get("username", "").strip(),
            request.form.get("password", ""),
        )
        if user:
            session["user_id"] = user["id"]
            session["username"] = user["username"]
            return redirect(url_for("dashboard"))
        flash("Invalid username or password.", "error")
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


@app.route("/dashboard")
@login_required
def dashboard():
    files = list_files(session["user_id"])
    return render_template("dashboard.html", files=files)


@app.route("/upload", methods=["POST"])
@login_required
def upload():
    saved = save_file(session["user_id"], request.files.get("file"))
    if saved:
        flash(f"Uploaded: {saved}", "success")
    else:
        flash("Invalid file or file type not allowed.", "error")
    return redirect(url_for("dashboard"))


@app.route("/download/<path:filename>")
@login_required
def download(filename):
    return send_from_directory(
        user_folder(session["user_id"]),
        secure_filename(filename),
        as_attachment=True,
    )


@app.route("/delete/<path:filename>", methods=["POST"])
@login_required
def delete(filename):
    if delete_file(session["user_id"], filename):
        flash(f"Deleted: {filename}", "success")
    else:
        flash("File not found.", "error")
    return redirect(url_for("dashboard"))


@app.errorhandler(413)
def too_large(_):
    flash("File too large (max 50 MB).", "error")
    return redirect(url_for("dashboard"))


if __name__ == "__main__":
    app.run(debug=True)
