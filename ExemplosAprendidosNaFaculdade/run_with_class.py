import sqlite3 as conector
from modelo import Pessoa

#Abertura da conexão # Aquisição de cursor
conexao = conector.connect('./dados/meu_banco.db')
cursor = conexao.cursor()
#Criação de um objeto do tipo Pessoa
pessoa = Pessoa(12345678901, 'Edmar', '1998-06-12', False)
#Definição de um comando com query parameter
comando = '''INSERT INTO Pessoa(cpf, nome, nascimento, oculos) VALUES (?,?,?,?);'''
cursor.execute(comando, (pessoa.cpf, pessoa.nome, pessoa.data_nascimento, pessoa.usa_oculos))

#Efetivação do comando
conexao.commit()
# Fechamento das conexoes
cursor.close()
conexao.close()