import sqlalchemy as sql
import sqlite3
import pandas as pd

class Conection:
    def __init__(self):
        self.conn = sqlite3.connect(r"Programas\torneio_bot\pontos.db") # conecta no banco de dados

        cursor = self.conn.cursor() # cria um cursor para conseguir fazer alterações no banco de dados

        # cria uma tabela
        cursor.execute("""CREATE TABLE IF NOT EXISTS users (
            Smogon INTEGER,
            JF INTEGER,
            Giovana INTEGER,
            Kedao INTEGER
            )""")

        # atualiza informações que o cursor fez no banco de dados
        self.conn.commit()

    def inserir(self, pontos: dict):
        cursor = self.conn.cursor()
        
        cursor.execute("""
        INSERT INTO users (Smogon, JF, Giovana, Kedao) VALUES (?,?,?,?)
        """, (pontos['smogon'], pontos['jf'], pontos['giovana'], pontos['kedao']))

        self.conn.commit()
        
    def exibir(self):
        cursor = self.conn.cursor()
        
        cursor.execute("""
        SELECT * FROM users
        """)

        pontos = cursor.fetchall()
        
        df = pd.DataFrame(pontos, columns=["Smogon", "JF", "Giovana", "Kedao"])
        
        return df
    

c = Conection()
c.exibir()
        
