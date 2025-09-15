import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

connection = mysql.connector.connect(
    host=os.getenv("HOST"),
    user=os.getenv("USER"),
    password=os.getenv("PASSWORD"),
    database=os.getenv("DATABASE"))

def create_table():
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS entries(
    content VARCHAR(255) NOT NULL,
    publication_date DATE NOT NULL)""")
    connection.commit()
    cursor.close()

def add_entry(entry_content: str, entry_date: str) -> None:
    cursor = connection.cursor()
    cursor.execute("INSERT INTO entries(content, publication_date) VALUES (%s, %s)", (entry_content, entry_date))
    connection.commit()
    cursor.close()

def get_entries():
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM entries")
    result = cursor.fetchall()
    cursor.close()
    return result
