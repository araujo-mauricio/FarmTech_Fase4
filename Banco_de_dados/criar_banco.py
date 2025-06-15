import sqlite3
from datetime import datetime
import random

# Conectar (ou criar) o banco de dados
conexao = sqlite3.connect('farmtech.db')
cursor = conexao.cursor()

# Criar a tabela sensores (se ainda não existir)
cursor.execute('''
CREATE TABLE IF NOT EXISTS sensores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data_hora TEXT,
    umidade REAL,
    nutriente REAL,
    irrigar INTEGER
)
''')

# Gerar 100 registros simulados de exemplo
for _ in range(100):
    umidade = random.uniform(20, 90)
    nutriente = random.uniform(10, 80)

    # Regra simplificada para irrigação:
    irrigar = 1 if umidade < 50 or nutriente < 30 else 0

    data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute('''
    INSERT INTO sensores (data_hora, umidade, nutriente, irrigar)
    VALUES (?, ?, ?, ?)
    ''', (data_hora, umidade, nutriente, irrigar))

# Salvar e encerrar a conexão
conexao.commit()
conexao.close()

print("Banco de dados 'farmtech.db' criado com sucesso!")
