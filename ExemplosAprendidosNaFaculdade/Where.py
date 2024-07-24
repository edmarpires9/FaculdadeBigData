import sqlite3 as conector
import modelo as Pessoa
conexao = conector.connect('./dados/meu_banco.db')
cursor = conexao.cursor()

comando = '''SELECT * FROM Pessoa WHERE oculos=:usa_oculos;'''
cursor.execute(comando, {'usa_oculos': True})

registros = cursor.fetchall()
for registro in registros:
    pessoa = Pessoa(*registro)
    print('cpf: ', pessoa.cpf)

    cursor.close()
    conexao.close()