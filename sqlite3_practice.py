import sqlite3
import datetime
from typing import Any

_PATH_DB = "financesx.db"


class Helper:

    @staticmethod
    def get_today_date() -> str:
        ''' Return today date as DD-MM-YYYY '''
        current_year: int = datetime.datetime.now().year
        current_month: int = datetime.datetime.now().month
        current_day: int = datetime.datetime.now().day
        return f"{current_day}-{current_month}-{current_year}"


class Database:

    @staticmethod
    def create_database() -> None:
        ''' Create database and tables '''
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
        conn.close()

    @staticmethod
    def insert_register(today: str, 
                        concept: str, 
                        amount: float,
                        category: str,
                        sub_category: str,
                        paid: int = 0,
                        payment_method: str = "HSBC Viva",
                        comments: str = "NA"
                        ) -> int | None:
        ''' Insert information into the database '''
        conn = sqlite3.connect(_PATH_DB)
        cursor = conn.cursor()

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

    @staticmethod
    def get_all_registers() -> list[Any]:
        ''' Return all the information in the database '''
        conn = sqlite3.connect(_PATH_DB)
        cursor = conn.cursor()
        cursor.execute('SELECT rowid, * FROM users')
        return cursor.fetchall()


register = (
    Helper.get_today_date(),  
    "Vacaciones", 
    230840.94,
    "Alimentos",
    "Despensa",
)

today = Helper.get_today_date()
Database.create_database()
Database.insert_register(*register)

for x in Database.get_all_registers():
    print(x)
