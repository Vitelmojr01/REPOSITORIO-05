
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import sys

print('Iniciando análise dos arquivos do SINASC...')

meses = sys.argv[1:]
mapa_meses = {'JAN':'01','FEV':'02','MAR':'03','ABR':'04','MAI':'05','JUN':'06',
              'JUL':'07','AGO':'08','SET':'09','OUT':'10','NOV':'11','DEZ':'12'}

for mes in meses:
    sinasc = pd.read_csv(f'SINASC_RO_2019_{mes}.csv')
    pasta = f'2019-{mapa_meses[mes]}'
    os.makedirs(pasta, exist_ok=True)

    plt.figure(figsize=(8,5))
    sns.histplot(sinasc['IDADEMAE'].dropna(), bins=20)
    plt.title(f'Idade da mãe - {mes}/2019')
    plt.savefig(f'{pasta}/idade_mae_{mes}.png')
    plt.show()