import sqlite3

# Conectar ao banco de dados
conexao = sqlite3.connect('db.db')

# Criar cursor para executar comandos SQL
cursor = conexao.cursor()


# Função para exibir os dados de um usuário em uma única linha
def exibir_usuario_por_id(id):
    # Executar a consulta SQL
    cursor.execute('SELECT nome, email, idade, profissao FROM usu WHERE id = ?', (id,))

    # Recuperar a linha retornada
    linha = cursor.fetchone()

    # Verificar se a linha existe
    if linha is not None:
        # Extrair os valores da linha
        nome, email, idade, profissao = linha

        # Exibir os dados em uma única linha
        print(f"Nome: {nome}, Email: {email}, Idade: {idade}, Profissão: {profissao}")
    else:
        print("Usuário não encontrado.")


# Exibir os usuários até o ID 10
for id in range(1, 11):
    exibir_usuario_por_id(id)
    print()

# Fechar a conexão com o banco de dados
conexao.close()
