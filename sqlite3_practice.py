import sqlite3
import datetime
from typing import Any

_PATH_DB = "financesx.db"


def get_today_date() -> str:
    ''' Return today |date as DD-MM-YYYY '''
    current_year: int = datetime.datetime.now().year
    current_month: int = datetime.datetime.now().month
    current_day: int = datetime.datetime.now().day
    return f"{current_day}-{current_month}-{current_year}"


def create_database() -> None:
    conn = sqlite3.connect(_PATH_DB)
    conn.close()


def insert_register() -> int | None:
    conn = sqlite3.connect(_PATH_DB)
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS users (
    date TEXT,
    name TEXT, 
    amount INTEGER,
    paid INTEGER,
    paid_date TEXT,
    payment_method TEXT,
    category TEXT,
    sub_category TEXT,
    comments TEXT)
    """)

    query = """INSERT INTO users VALUES (
    ?, ?, ?, ?, ?, ?, ?, ?, ?
    );"""  # 9

    cursor.execute(query, (
        today, 
        "Costco", 
        7003.94,
        0,
        today,
        "HSBC Viva",
        "Alimentos",
        "Despensa",
        "NA")
    )
    conn.commit()
    return cursor.lastrowid


def return_all_registers() -> list[Any]:
    conn = sqlite3.connect(_PATH_DB)
    cursor = conn.cursor()
    cursor.execute('SELECT rowid, * FROM users')
    return cursor.fetchall()


today = get_today_date()
create_database()
insert_register()

for x in return_all_registers():
    print(x)
