import sqlite3

# Conectar ao banco de dados
conexao = sqlite3.connect('db.db')

# Criar cursor para executar comandos SQL
cursor = conexao.cursor()


# Função para exibir os dados de um usuário em uma única linha
def exibir_usuario_por_id(id):
    # Executar a consulta SQL
    cursor.execute('SELECT * FROM usu WHERE id = ?', (id,))

    # Recuperar a linha retornada
    linha = cursor.fetchone()

    # Verificar se a linha existe
    if linha is not None:
        # Extrair os valores da linha
        id, nome, email, idade, profissao = linha

        # Exibir os dados em uma única linha
        print(f"ID: {id}, Nome: {nome}, Email: {email}, Idade: {idade}, Profissão: {profissao}")
    else:
        print("Usuário não encontrado.")


# Solicitar a entrada do ID do usuário
id_escolhido = input("Digite o ID do usuário que deseja exibir: ")

# Converter o ID digitado para inteiro
id_escolhido = int(id_escolhido)

# Exibir o usuário com o ID escolhido
exibir_usuario_por_id(id_escolhido)

# Fechar a conexão com o banco de dados
conexao.close()
