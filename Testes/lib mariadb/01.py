# execute o cmd como administrador e ligue o mariaDB com: net start mariadb

import mariadb
from dotenv import load_dotenv
import os

load_dotenv()
db_password = os.getenv("MARIA_PASSWORD") # senha do DB

conexão = mariadb.connect(
    user = "root", # nome do usuario
    password = db_password, 
    host= "localhost",
    database= "exemplo" # tambem pode ser um dominio(meusite.com) ou um endereço ip(192.168.1.100)
)
"""
host="localhost": Quando o banco de dados está na mesma máquina.
host="192.168.1.100": Quando o banco de dados está em uma máquina com esse IP na rede local.
host="db.exemplo.com": Quando o banco de dados está acessível via nome de domínio.
"""

cursor = conexão.cursor() # cria um cursor para se comunicar com o DB 

cursor.execute("SELECT * FROM users") # executa uma query com o banco

print(cursor.fetchall())

cursor.close()
conexão.close()