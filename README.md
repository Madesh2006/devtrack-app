<div align="center">

# ⚡ DevTrack — Developer Task Manager

<p align="center">
  <strong>A clean, responsive task dashboard built with Python, Flask, SQLite, HTML, and CSS.</strong><br>
  Track tasks across projects, set priorities and due dates, and update progress from one place.
</p>

<!-- Typing SVG animation banner -->
<a href="https://github.com/Madesh2006/devtrack-app">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=20&pause=1000&color=38BDF8&center=true&vCenter=true&width=550&lines=Track+tasks+across+projects;Set+priorities+and+due+dates;Filter+by+status+and+search+instantly;Manage+everything+in+one+place" alt="Typing SVG" />
</a>

<br><br>

<!-- Badges -->
<img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/Flask-Framework-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask" />
<img src="https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite" />
<img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5" />
<img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3" />
<img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License" />

</div>

---

## 📖 Overview

**DevTrack** is a lightweight, self-hosted web application designed to help developers organize project workflows with minimal overhead. It eliminates cluttered interfaces in favor of a fast, local dashboard with quick search, priority tagging, and automated sample data initialization.

---

## ✨ Features

- 📝 **Task Management:** Create, view, update, and delete development tasks effortlessly.
- 🔄 **Status Workflow:** Track items across `Todo`, `In Progress`, and `Done`.
- 🎯 **Priority Levels:** Assign `High`, `Medium`, or `Low` priority tags with distinct visual cues.
- 📅 **Project & Schedule Tracking:** Group tasks by project names and attach target due dates.
- 🔍 **Instant Search:** Quickly filter and find tasks by title, description, or project name.
- 🏷️ **Status Filtering:** Switch views between all tasks and specific status buckets with a click.
- 📊 **Dashboard Metrics:** Real-time summary counters showing total tasks, completed work, and active projects.
- 📱 **Fully Responsive:** Optimized UI for desktop browsers, tablets, and mobile screens.
- 🗄️ **Zero Setup DB:** SQLite database auto-provisions tables and inserts 3 starter tasks on initial startup.
- 💓 **Health Check Endpoint:** Ready for uptime monitors and container probes via `/health`.

---

## 🖥️ Preview

Run the app locally to explore the dashboard. The first launch automatically creates the local `database.db` SQLite file and populates sample tasks so you can get started immediately.

---

## 🛠️ Tech Stack & Architecture

| Layer | Technology | Purpose |
| :--- | :--- | :--- |
| **Backend** | Python 3.10+, Flask | Routing, server-side templating, and REST API |
| **Database** | SQLite 3 | Embedded, serverless local storage |
| **Frontend** | HTML5, CSS3, Jinja2 | Responsive layout, dark/light styling, and UI components |
| **Environment** | `python-dotenv` | Config and secret management via `.env` |

---

## 📂 Project Structure

```text
devtrack-app/
├── static/              # CSS styling, JavaScript, and static assets
├── templates/           # Jinja2 HTML templates
├── .env.example         # Environment template configuration
├── .gitignore           # Git ignore rules for venv, cache, and db files
├── app.py               # Main Flask application logic and database setup
├── LICENSE              # Project license
├── README.md            # Documentation and instructions
└── requirements.txt     # Python dependencies
