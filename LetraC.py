import sqlite3

# Conectar ao banco de dados
conexao = sqlite3.connect('db.db')

# Criar cursor para executar comandos SQL
cursor = conexao.cursor()

# Executar a consulta SQL
cursor.execute('SELECT * FROM usu')

# Recuperar todas as linhas retornadas
linhas = cursor.fetchall()

# Exibir as linhas retornadas
for linha in linhas:
    id, nome, email, idade, profissao = linha
    print("ID:", id)
    print("Nome:", nome)
    print("Email:", email)
    print("Idade:", idade)
    print("Profissão:", profissao)
    print()

# Fechar a conexão com o banco de dados
conexao.close()
