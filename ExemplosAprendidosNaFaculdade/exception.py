import remove

nome_antigo = "texto01.txt"
nome_novo = "texto02.txt"

try:
    os.rename(nome_antigo, nome_novo)
    print('Arquivo renomeado')
except FileNotFoundError:
    print('Arquivo não encontrado')
except Exception as e:
    print(f'Erro generíco {e}')