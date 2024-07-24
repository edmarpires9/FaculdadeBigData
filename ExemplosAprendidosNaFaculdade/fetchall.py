import sqlite3 as conector
#Abertura da conexão
conexao = conector.connect('./dados/meu_banco.db')
cursor = conexao.cursor()

#Definição dos registros
comando = '''SELECT nome, oculos FROM Pessoas;'''
cursor.execute(comando)

#Recuperação de dados
registros = cursor.fetchall()
print('Tipo retornado pelo fecthall(): ', type(registros))

for registro in registros:
    print('Tipo:', type(registro), ' - Conteúdo:', registro)

#Fechando das conexões
cursor.close()
conexao.close()