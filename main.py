#Importação das bibliotecas
#Panda uma excelente alternativa rápida e confiavél para realizar a leitura de tabelas do Excel.
import pandas as pd
#Matplotlib uma ferramenta para gerar gráficos com facilidade
import matplotlib.pyplot as plt
# Função para ler o arquivo
def ler_tabela(caminho_do_arquivo):
    if caminho_do_arquivo.endswith('.csv'):
        tabela = pd.read_csv(caminho_do_arquivo)
    elif caminho_do_arquivo.endswith('xlsx'):
        tabela = pd.read_excel(caminho_do_arquivo, engine='openpyxl')
    else:
        raise ValueError('Erro de leitura o arquivo selecionado não corresponde aos formatos suportados .CSV ou .XLSX.')
    return tabela

#Função para contar os nomes de onde faltou energia
def contar_nomes(tabela,nome_da_coluna):
    contagem_de_nomes = tabela[nome_da_coluna].value_counts()
    return contagem_de_nomes

#Função para gerar o gráfico
def gerar_grafico(contagem_de_nomes, top_n=10):
    top_nomes = contagem_de_nomes.head(top_n)
    plt.figure(figsize=(10,6))
    top_nomes.plot(kind='bar')
    plt.title(f'Nome dos locais onde o fornecimento de energia é interrompido com maior frequência.')
    plt.xlabel('Nome do local.')
    plt.ylabel('Quantidade de interrupção.')
    plt.xticks(rotation = 45)
    plt.tight_layout()
    plt.show()

#Caminho da tabela do Excel a mesma deve estar no formato .CSV ou XLSX
caminho_do_arquivo = 'db.xlsx'
nome_da_coluna = 'Descrição'

#Chama a função que realiza leitura da tabela do Excel
tabela = ler_tabela(caminho_do_arquivo)

#Chama a função que conta quantas vezes faltou energia em cada local
contagem_de_nomes = contar_nomes(tabela, nome_da_coluna)

#Gera o gráfico contendo apenas os 10x locais onde faltou energia com maior frequência para que seja efetivado uma manutenção na rede de distribuição de energia.
gerar_grafico(contagem_de_nomes, top_n=10)