# 📝 Programming Diary

A simple **Programming Diary** application built in Python with **MySQL**.  
Track what you've learned each day, view past entries, and keep your progress organized.  

---

## 📌 Features
- Add new diary entries with content and date  
- View all past entries in chronological order  
- Stores data in a **MySQL database**  
- Lightweight and easy to use via the command-line interface (CLI)  

---

## 🗂 Project Structure

    ├── main.py # Main program, CLI interface
    ├── database.py # Database connection and helper functions
    └── README.md # Project documentation

---

## ▶️ Requirements
- Python 3.8+  
- MySQL server installed and running  
- Python package: `mysql-connector-python`

    **Install dependencies:**
    ```bash
    pip install mysql-connector-python

---

## 🏁 Setup & Run

1. Make sure MySQL is running and credentials in database.py match your server:
    ```python
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456789",
        database="data"
    )

2. Create the database (if not already):
    ```sql
   CREATE DATABASE data;

3. Run the program:
    ```bash
   python main.py

---

## 🧑‍💻 Example Usage

    welcome to the programming diary!
    
    please select one of the following options:
    1) Add new entry for today
    2) View all entries
    3) Exit.
    
    Your selection: 1
    What have you learned today?: Learned about Python classes and OOP
    Enter the date: 2025-09-16
    
    please select one of the following options:
    1) Add new entry for today
    2) View all entries
    3) Exit.
    
    Your selection: 2
    2025-09-16
    Learned about Python classes and OOP

---
