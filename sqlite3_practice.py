import sqlite3
import datetime

_PATH_DB = "financesx.db"

# get today date
current_year = datetime.datetime.now().year
current_month = datetime.datetime.now().month
current_day = datetime.datetime.now().day
today = str(current_day) + "-" + str(current_month) + "-" + str(current_year)

# create database
conn = sqlite3.connect(_PATH_DB)
cursor = conn.cursor()

# create table
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

# insert information
query = """INSERT INTO users VALUES (
    ?, ?, ?, ?, ?, ?, ?, ?, ?
    );""" # 9

# insert the data into table
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

# select information and print
cursor.execute('SELECT rowid, * FROM users')

result = cursor.fetchall()
for row in result:
    print(row)


'''
Id	
Fecha
Concepto
Cantidad
Pagado (Verdadero o Falso)
Fecha en la que se pago (Fecha como TEXTO)
Forma de pago (Especificar la tarjeta o Efectivo)
Categoria (Alimentos, Transportes, etc.)
Subcategoria (Restaurantes, etc.)
Comentarios (Cualquier comentario)
'''
