#Utilizando o metodo open() para escolher um arquivo.
arquivo = open("dados/texto.txt", "r")
#Salvando o conteudo do arquivo como uma string dentro de outra variável
texto = arquivo.read()
#Exibindo no console a variável texto
print(texto)