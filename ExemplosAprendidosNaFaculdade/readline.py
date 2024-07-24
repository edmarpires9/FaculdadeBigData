#Utilizando o metodo open() para escolher um arquivo.
arquivo = open("dados/texto.txt", "r")
#Salvando o conteudo de uma linha na variável
texto = arquivo.readline()
#Exibindo no console a variável texto
print(texto)