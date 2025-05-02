import mariadb
from dotenv import load_dotenv
import os

load_dotenv()
db_password = os.getenv("MARIA_PASSWORD")
try:
    conexao = mariadb.connect(
        user="root",          # Usuário
        password=f"{db_password}", # Senha do usuário
        host="localhost",     # Endereço do servidor (use o IP se não for localhost)
        database="exemplo"    # Nome do banco de dados
    )

    # Criando um cursor
    cursor = conexao.cursor()

    # Inserindo dados na tabela
    nome = "Ana"
    idade = 22
    cursor.execute("INSERT INTO users (nome, idade) VALUES (?, ?)", (nome, idade))

    # Commitando a transação
    conexao.commit()

    print(f"{cursor.rowcount} registro(s) inserido(s) com sucesso!")

except mariadb.Error as e:
    print(f"Erro ao conectar ou executar a consulta: {e}")

finally:
    # Fechando a conexão
    if conexao:
        cursor.close()
        conexao.close()
        print("Conexão fechada.")
