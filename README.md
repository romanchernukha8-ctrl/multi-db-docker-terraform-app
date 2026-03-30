# 🚀 Multi-DB Terraform + Podman App

##  Overview

This project demonstrates a Python application working with **two databases in parallel**:

* SQLite (local file-based database)
* MySQL (provisioned and managed via Terraform in a container)

The main goal of the project is to showcase:

* Infrastructure as Code using Terraform
* Container management with Podman
* Parallel data access from multiple databases in Python

---

##  Tech Stack

* Python 3.11
* Terraform
* Podman
* MySQL 8
* SQLite

---

##  Project Structure

```
.
├── app/
│   ├── app.py
│   ├── db/
│   │   ├── mysql_db.py
│   │   └── sqlite_db.py
│   ├── requirements.txt
│   └── .env
│
├── terraform/
│   ├── mysql/
│   └── podman/
│
└── README.md
```

---

## How It Works

1. Terraform provisions a MySQL container using Podman
2. Python application connects to:

   * local SQLite database
   * MySQL container
3. Data is fetched from both databases in parallel

---

## How to Run

### 1. Initialize and apply Terraform

```
cd terraform/mysql
terraform init
terraform apply
```

---

### 2. Run application

```
cd app
python3 -m app.app
```

---

##  Example Output

```
MySQL connected!
SQLite: [...]
MySQL: [...]
```

---

##  Features

* Parallel work with multiple databases
* Infrastructure managed via Terraform
* MySQL container managed by Podman
* Automatic database initialization
* Clean modular Python structure

---

##  Future Improvements

* Add remote Terraform state (S3)
* Add CI/CD pipeline
* Add environment separation (dev/prod)
* Deploy to AWS (RDS)

---
