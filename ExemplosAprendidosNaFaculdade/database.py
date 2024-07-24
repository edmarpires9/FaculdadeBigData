import sqlite3 as conector
#Também pode ser utilizado um banco temporário com sqlite3.connect(':memory:')

try:
    conexao = conector.connect('./dados/meu_banco.db')
    cursor = conexao.cursor()
    #Comando 01
    # comando = '''CREATE TABLE Pessoa (
    # cpf INTEGER NOT NULL,
    # nome TEXT NOT NULL,
    # nascimento DATE NOT NULL,
    # oculos BOOLEAN NOT NULL,
    # PRIMARY KEY (cpf)
    # );'''
    #Comando 02
    # comando = '''CREATE TABLE Marca ( id INTEGER NOT NULL,
    # nome TEXT NOT NULL,
    # sigla CHARACTER(2) NOT NULL,
    # PRIMARY KEY(id)
    # );'''
    #Comando 03
#     comando = '''CREATE TABLE Veiculo (
# placa CHARACTER(7) NOT NULL,
# ano INTEGER NOT NULL,
# cor TEXT NOT NULL,
# proprietario INTEGER NOT NULL,
# marca INTEGER NOT NULL,
# PRIMARY KEY (placa),
# FOREIGN KEY(proprietario) REFERENCES Pessoa(cpf),
# FOREIGN KEY(marca) REFERENCES Marca(id)
# );'''
    #Comando 04
#     comando = '''ALTER TABLE Veiculo
# ADD motor REAL;'''
    #Comando 05
#     comando = '''DROP TABLE Veiculo;
# '''
    #Comando 06
#     comando = '''CREATE TABLE Veiculo (
# placa CHARACTER(7) NOT NULL,
# ano INTEGER NOT NULL,
# cor TEXT NOT NULL,
# motor REAL NOT NULL,
# proprietario INTEGER NOT NULL,
# marca INTEGER NOT NULL,
# PRIMARY KEY (placa),
# FOREIGN KEY(proprietario) REFERENCES Pessoa(cpf),
# FOREIGN KEY(marca) REFERENCES Marca(id)
# );'''
#     #Comando 07
#     comando = '''INSERT INTO Pessoa (cpf, nome, nascimento, oculos)
#     VALUES (12345678900, 'João', '2000-01-31', 1);
#     '''
    cursor.execute(comando)
    conexao.commit()
except conector.DatabaseError as err:
    print('Erro de banco de dados', err)
finally:
    if conexao:
        cursor.close()
        conexao.close()