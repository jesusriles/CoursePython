import sqlite3
import datetime
from typing import Any
from pydantic import BaseModel, Field

_PATH_DB = "finances.db"


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
        ''' Create the database and the required tables. '''
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
    def insert_register(reg: Register) -> int | None:
        ''' Insert information into the database. '''
        conn = sqlite3.connect(_PATH_DB)
        cursor = conn.cursor()

        query = """INSERT INTO users VALUES (
        ?, ?, ?, ?, ?, ?, ?, ?, ?
        );"""  # 9

        cursor.execute(query, (
            reg.date, 
            reg.concept, 
            reg.amount,
            reg.paid,
            reg.paid_date,
            reg.payment_method,
            reg.category,
            reg.sub_category,
            reg.comments)
        )
        conn.commit()
        return cursor.lastrowid

    @staticmethod
    def get_all_registers() -> list[Any]:
        ''' Return all the information in the database. '''
        conn = sqlite3.connect(_PATH_DB)
        cursor = conn.cursor()
        cursor.execute('SELECT rowid, * FROM users')
        return cursor.fetchall()

    @staticmethod
    def get_all_categories() -> list[Any]:
        ''' Return all the categories. '''
        conn = sqlite3.connect(_PATH_DB)
        cursor = conn.cursor()
        cursor.execute('SELECT DISTINCT category FROM users;')
        return cursor.fetchall()


class Register(BaseModel):
    date: str = Field(default_factory=Helper.get_today_date)
    concept: str = Field(min_length=1, max_length=100)
    amount: float = Field(gt=0)
    category: str = Field(default="Empty", min_length=1, max_length=20)
    sub_category: str = Field(default="Empty", min_length=1, max_length=20)
    paid: bool = False
    paid_date: str = Field(default="Empty")
    payment_method: str = Field(default="Empty")
    comments: str = Field(default="Empty", max_length=255)


register = Register(concept="Hello World", 
                    amount=99.80, 
                    )

Database.create_database()
Database.insert_register(register)

registers = Database.get_all_registers()
for register in registers:
    print(register)

categories = Database.get_all_categories()
print(categories)
