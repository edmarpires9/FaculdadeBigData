#Exemplo 01
with open('dados/texto.txt', 'r') as arquivo:
    texto = arquivo.read()
    contagem01 = texto.count('Linha')
    print(contagem01)

#Exemplo 02 - Atenção observe que o programa contabiliza a palavra amador
linha02 = 'Amar ama amador'
contagem02 = linha02.count('ama')
print('Exemplo 02: ', contagem02)

#Exemplo 03 - Após a aplicação do metodo split a contagem é realizada com maior precisão
linha03 = 'Amar ama amador'
linha03split = linha03.split()
contagem03 = linha03split.count('ama')
print(contagem03)