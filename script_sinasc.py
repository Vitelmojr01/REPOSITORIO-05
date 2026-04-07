import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

print('Iniciando análise dos arquivos do SINASC...')

# lista dos meses pedidos na tarefa
meses = ['MAR', 'ABR', 'MAI', 'JUN', 'DEZ']

# cria a pasta onde os gráficos serão salvos
os.makedirs('graficos_sinasc', exist_ok=True)
print('Pasta "graficos_sinasc" pronta.')

for mes in meses:
    print(f'\nLendo a base do mês: {mes}')
    
    caminho_arquivo = f'SINASC_RO_2019_{mes}.csv'
    sinasc = pd.read_csv(caminho_arquivo)
    
    print(f'Base {mes} carregada com sucesso.')
    print(f'Quantidade de linhas: {sinasc.shape[0]}')
    print(f'Quantidade de colunas: {sinasc.shape[1]}')

    # gráfico 1 - idade da mãe
    plt.figure(figsize=(8,5))
    sns.histplot(sinasc['IDADEMAE'].dropna(), bins=20)
    plt.title(f'Idade da mãe - {mes}/2019')
    plt.xlabel('Idade da mãe')
    plt.ylabel('Frequência')
    plt.savefig(f'graficos_sinasc/idade_mae_{mes}.png')
    plt.show()
    print(f'Gráfico de idade da mãe do mês {mes} salvo com sucesso.')

    # gráfico 2 - escolaridade da mãe
    plt.figure(figsize=(8,5))
    sinasc['ESCMAE'].value_counts().sort_index().plot.bar()
    plt.title(f'Escolaridade da mãe - {mes}/2019')
    plt.xlabel('Escolaridade')
    plt.ylabel('Quantidade')
    plt.savefig(f'graficos_sinasc/escolaridade_mae_{mes}.png')
    plt.show()
    print(f'Gráfico de escolaridade da mãe do mês {mes} salvo com sucesso.')

    # gráfico 3 - consultas pré-natal
    plt.figure(figsize=(8,5))
    sinasc['CONSULTAS'].value_counts().sort_index().plot.bar()
    plt.title(f'Consultas pré-natal - {mes}/2019')
    plt.xlabel('Número de consultas')
    plt.ylabel('Quantidade')
    plt.savefig(f'graficos_sinasc/consultas_{mes}.png')
    plt.show()
    print(f'Gráfico de consultas do mês {mes} salvo com sucesso.')

print('\nTodos os gráficos foram gerados com sucesso.')