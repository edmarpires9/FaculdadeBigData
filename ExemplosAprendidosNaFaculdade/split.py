with open('dados/texto.txt', 'r') as arquivo:
    texto = arquivo.read()
    metodoSplit = texto.split('a')
    print(metodoSplit)