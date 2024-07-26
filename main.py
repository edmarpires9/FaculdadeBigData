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


