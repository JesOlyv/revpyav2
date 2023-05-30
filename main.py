import sqlite3

# Conectar ao banco de dados
conexao = sqlite3.connect('db.db')

# Criar cursor para executar comandos SQL
cursor = conexao.cursor()

# Criar tabela usu
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usu (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        email TEXT,
        idade INTEGER,
        profissao TEXT
    )
''')

# Dados dos usuários
usuarios = [
    ('João', 'joao@example.com', 25, 'Engenheiro'),
    ('Maria', 'maria@example.com', 30, 'Advogada'),
    ('Pedro', 'pedro@example.com', 28, 'Programador'),
    ('Ana', 'ana@example.com', 32, 'Médica'),
    ('Lucas', 'lucas@example.com', 27, 'Designer'),
    ('Carla', 'carla@example.com', 29, 'Professora'),
    ('Gustavo', 'gustavo@example.com', 31, 'Empresário'),
    ('Laura', 'laura@example.com', 26, 'Contadora'),
    ('Mariana', 'mariana@example.com', 33, 'Arquiteta'),
    ('Ricardo', 'ricardo@example.com', 35, 'Engenheiro'),
    ('Fernanda', 'fernanda@example.com', 24, 'Publicitária'),
    ('Paulo', 'paulo@example.com', 40, 'Médico')
]

# Inserir os usuários na tabela
cursor.executemany('INSERT INTO usu (nome, email, idade, profissao) VALUES (?, ?, ?, ?)', usuarios)

# Salvar as alterações no banco de dados
conexao.commit()

# Fechar a conexão com o banco de dados
conexao.close()
