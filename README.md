# 🚀 Multi-DB Docker + Terraform App

## 🧠 Overview

This project demonstrates a Python application working with **two databases simultaneously**:

* SQLite (local file-based database)
* MySQL (running in a Docker container)

The project showcases:

* Infrastructure as Code using Terraform
* Container orchestration with Docker Compose
* Multi-database integration in Python

---

## 🏗️ Tech Stack

* Python 3.11
* Docker & Docker Compose
* Terraform
* MySQL 8
* SQLite

---

## 📁 Project Structure

```
.
├── app/
│   ├── app.py
│   ├── db/
│   │   ├── mysql_db.py
│   │   └── sqlite_db.py
│   ├── Dockerfile
│   ├── requirements.txt
│   └── .env
│
├── terraform/
│   ├── mysql/
│   ├── sqlite/
│   └── podman/
│
├── docker-compose.yml
└── README.md
```

---

## ⚙️ How to Run

### 1. Clone repository

```
git clone https://github.com/romanchernukha8-ctrl/multi-db-docker-terraform-app.git
cd multi-db-docker-terraform-app
```

---

### 2. Run application

```
docker compose up --build
```

---

## 📊 Expected Output

```
MySQL connected!
SQLite: [...]
MySQL: [...]
```

---

## ⚠️ Important Notes

* The application includes retry logic for MySQL connection
* Containers communicate via Docker internal network
* MySQL may take a few seconds to start — this is handled automatically

---

## 🔥 Features

* Multi-database support (SQLite + MySQL)
* Infrastructure provisioning with Terraform
* Fully containerized environment
* Automatic database initialization
* Clean project structure

---

## 📈 Future Improvements

* Add REST API (FastAPI)
* Add CI/CD (GitHub Actions)
* Deploy to AWS
* Add monitoring/logging

---

## 👨‍💻 Author

Roman Chernukha
