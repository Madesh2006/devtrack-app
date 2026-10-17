# DevTrack — Developer Task Manager

A clean, responsive task dashboard built with **Python, Flask, SQLite, HTML, and CSS**. Track tasks across projects, set priorities and due dates, and update progress from one place.

## Features

- Create and delete tasks
- Track status: Todo, In Progress, Done
- Set High, Medium, or Low priority
- Add project names and due dates
- Search by task or project
- Filter tasks by status
- Dashboard stats for tasks, completed work, and projects
- Responsive layout for desktop, tablet, and mobile
- SQLite database initializes automatically with sample tasks
- Health endpoint at `/health`

## Preview

Run the app locally to explore the dashboard. The first launch creates a local SQLite database and adds three example tasks.

## Tech stack

- Python 3.10+
- Flask
- SQLite
- HTML5 and CSS3

## Run locally

### 1. Clone your repository

```bash
git clone https://github.com/YOUR-USERNAME/devtrack.git
cd devtrack
```

Replace `YOUR-USERNAME/devtrack` with your GitHub repository URL.

### 2. Create a virtual environment

**Windows PowerShell**
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, you can use the environment's Python directly:
```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe app.py
```

**macOS / Linux**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Start the app

```bash
python app.py
```

Open **http://127.0.0.1:5000** in your browser.

The SQLite database (`devtrack.db`) is created automatically and is intentionally excluded from Git.

## Push this project to GitHub

Create an **empty repository** on GitHub named `devtrack`. Do not add a README or `.gitignore` on GitHub if you already have these files locally.

Then, from this project folder:

```bash
git init
git add .
git commit -m "Initial commit: DevTrack task manager"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/devtrack.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your GitHub username.

### If `origin` already exists

```bash
git remote -v
git remote set-url origin https://github.com/YOUR-USERNAME/devtrack.git
git push -u origin main
```

### If GitHub says the remote contains work you do not have

If the remote has a README or other commits, integrate them before pushing:

```bash
git pull --rebase origin main
git push -u origin main
```

If there are merge conflicts, resolve them first. Avoid force-pushing unless you fully understand which remote changes would be overwritten.

## Project structure

```text
devtrack/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env.example
├── templates/
│   └── index.html
└── static/
    └── style.css
```

## Routes

| Route | Purpose |
|---|---|
| `GET /` | Dashboard, search, and filters |
| `POST /tasks` | Create a task |
| `POST /tasks/<id>/status` | Update task status |
| `POST /tasks/<id>/delete` | Delete a task |
| `GET /health` | Basic health check |

## Production notes

- Set a strong, private Flask secret key before deploying.
- Turn off Flask debug mode in production.
- Use a production WSGI server such as Gunicorn on supported hosts.
- SQLite is suitable for a small demo; consider PostgreSQL for a multi-user deployment.
- Add authentication and CSRF protection before exposing the app publicly.

## Roadmap ideas

- User login and personal workspaces
- Kanban board with drag-and-drop
- Project-specific dashboards
- Task comments and attachments
- Email reminders and calendar integration
- PostgreSQL support and automated tests

## License

MIT — see `LICENSE`.
