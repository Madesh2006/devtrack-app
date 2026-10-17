from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "devtrack.db"
app = Flask(__name__)
app.secret_key = "change-this-secret-key-before-production"

def connect_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with connect_db() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                project TEXT NOT NULL DEFAULT 'Personal',
                priority TEXT NOT NULL DEFAULT 'Medium',
                status TEXT NOT NULL DEFAULT 'Todo',
                due_date TEXT,
                created_at TEXT NOT NULL
            )
        """)
        count = conn.execute("SELECT COUNT(*) FROM tasks").fetchone()[0]
        if count == 0:
            examples = [
                ("Design portfolio homepage", "Portfolio Website", "High", "In Progress", "2026-10-22"),
                ("Write project README", "DevTrack", "Medium", "Todo", "2026-10-20"),
                ("Review API routes", "NeuroVoice AI", "Low", "Done", "2026-10-15"),
            ]
            for title, project, priority, status, due_date in examples:
                conn.execute(
                    "INSERT INTO tasks (title, project, priority, status, due_date, created_at) VALUES (?, ?, ?, ?, ?, ?)",
                    (title, project, priority, status, due_date, datetime.now().isoformat(timespec="seconds"))
                )

@app.route("/")
def index():
    status_filter = request.args.get("status", "All")
    search = request.args.get("q", "").strip()
    query = "SELECT * FROM tasks WHERE 1=1"
    params = []
    if status_filter in ("Todo", "In Progress", "Done"):
        query += " AND status = ?"
        params.append(status_filter)
    if search:
        query += " AND (title LIKE ? OR project LIKE ?)"
        params.extend([f"%{search}%", f"%{search}%"])
    query += " ORDER BY CASE priority WHEN 'High' THEN 1 WHEN 'Medium' THEN 2 ELSE 3 END, id DESC"
    with connect_db() as conn:
        tasks = conn.execute(query, params).fetchall()
        stats = {
            "total": conn.execute("SELECT COUNT(*) FROM tasks").fetchone()[0],
            "active": conn.execute("SELECT COUNT(*) FROM tasks WHERE status != 'Done'").fetchone()[0],
            "done": conn.execute("SELECT COUNT(*) FROM tasks WHERE status = 'Done'").fetchone()[0],
            "projects": conn.execute("SELECT COUNT(DISTINCT project) FROM tasks").fetchone()[0],
        }
    return render_template("index.html", tasks=tasks, stats=stats, status_filter=status_filter, search=search)

@app.route("/tasks", methods=["POST"])
def add_task():
    title = request.form.get("title", "").strip()
    project = request.form.get("project", "Personal").strip() or "Personal"
    priority = request.form.get("priority", "Medium")
    due_date = request.form.get("due_date") or None
    if not title:
        flash("Please enter a task title.", "error")
    elif priority not in ("Low", "Medium", "High"):
        flash("Choose a valid priority.", "error")
    else:
        with connect_db() as conn:
            conn.execute(
                "INSERT INTO tasks (title, project, priority, status, due_date, created_at) VALUES (?, ?, ?, 'Todo', ?, ?)",
                (title, project, priority, due_date, datetime.now().isoformat(timespec="seconds"))
            )
        flash("Task added successfully.", "success")
    return redirect(url_for("index"))

@app.route("/tasks/<int:task_id>/status", methods=["POST"])
def update_status(task_id):
    status = request.form.get("status")
    if status in ("Todo", "In Progress", "Done"):
        with connect_db() as conn:
            conn.execute("UPDATE tasks SET status = ? WHERE id = ?", (status, task_id))
        flash("Task status updated.", "success")
    return redirect(url_for("index"))

@app.route("/tasks/<int:task_id>/delete", methods=["POST"])
def delete_task(task_id):
    with connect_db() as conn:
        conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    flash("Task deleted.", "success")
    return redirect(url_for("index"))

@app.route("/health")
def health():
    return {"status": "ok", "app": "DevTrack"}

init_db()

if __name__ == "__main__":
    app.run(debug=True)
