# 🚀 Navigator DB Manager

A lightweight, interactive Command Line Interface (CLI) built in Python to manage and interact with multiple SQL databases seamlessly. Whether you need to inspect tables, run custom queries, or manage data across different environments, Navigator provides a centralized, color-coded terminal experience.

---

## ✨ Features

* **Multi-Engine Support:** Connects to PostgreSQL, MySQL, MariaDB, and SQL Server (MSSQL).
* **Interactive Dashboard:** User-friendly menu for quick database operations.
* **Data Visualization:** Uses `PrettyTable` for clean, readable table rendering in the terminal.
* **Secure Input:** Hidden password entry using `pwinput`.
* **SQL Execution:** Execute custom `INSERT`, `UPDATE`, `DELETE`, or `ALTER` commands directly from the prompt.
* **Database Inspection:** Easily list all databases, tables, and column structures.

---

## 🛠️ Prerequisites

Before you start, make sure you have the following Python libraries installed:

```bash
pip install sqlalchemy prettytable colorama pwinput requests psycopg2 mysql-connector-python mariadb pyodbc

```

> **Note:** Depending on your database of choice, you might only need specific drivers (e.g., `psycopg2` for PostgreSQL).

---

## 🚀 Getting Started

1. **Clone the Repository:**
```bash
git clone https://github.com/yourusername/navigator-db-manager.git
cd navigator-db-manager

```


2. **Run the Application:**
```bash
python main.py

```


3. **Connection Setup:**
* Select your **Database Type** (PostgreSQL, MySQL, etc.).
* Enter the **IP/URL** of the database server.
* Provide the **Username** and **Password** (Input is masked for security).
* Choose a custom **Port** or hit `ENTER` to use the default port for that database type.



---

## 🖥️ Usage Guide

Once connected, you can perform the following actions through the main dashboard:

1. **List Databases:** Scans the server and displays all available database names.
2. **Enter Database:** Switch between different databases on the same server.
3. **List Tables:** Show all table names within the current database.
4. **Read Table:** Select a table to view its contents in a clean, formatted grid.
5. **Run SQL Command:** A sandbox to execute raw SQL queries (e.g., `INSERT INTO`, `DROP TABLE`, etc.) with automatic transaction commits.

---

## 🗂️ Tech Stack

* **Language:** Python 3.x
* **Database ORM:** [SQLAlchemy]()
* **CLI Styling:** [Colorama]()
* **Formatting:** [PrettyTable]()
* **Security:** [pwinput]()

---

## 🤝 Contribution

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page]().

---

## 👤 Author

**MIGRDEV**

* **Discord:** `migrdev_buy`
