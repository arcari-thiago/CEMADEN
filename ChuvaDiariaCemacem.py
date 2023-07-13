# -*- coding: utf-8 -*-
"""
Created on Mon May 11 16:31:29 2020

@author: ThiLau
"""

import pandas as pd
import matplotlib.pyplot as plt


filename = "jun2023.csv" # arquivo com os dados brutos do pluviógrafo
local = "Rio Sangão"

# Leitura do arquivo CSV e conversão da coluna 'datahora' para tipo datetime
dados = pd.read_csv(filename, sep=';', parse_dates=['datahora'])

# Filtragem das linhas com base no local
dados_local = dados[dados['nomeEstacao'] == local]

# Transformações dos dados
dados_local['Data'] = pd.to_datetime(dados_local['datahora']).dt.date
dados_local['Precipitação (mm)'] = dados_local['valorMedida'].str.replace('.', '').str.replace(',', '.').astype(float)

# Agrupamento e soma da precipitação diária
chuva_diaria = dados_local.groupby('Data')['Precipitação (mm)'].sum()

# Criar DataFrame com as colunas renomeadas
chuva_diaria = chuva_diaria.reset_index().rename(columns={'Data': 'Data', 'Precipitação (mm)': 'Precipitação (mm)'})

# Salvando os resultados em um arquivo Excel
chuva_diaria.to_excel('chuva_diaria_jun2023.xlsx', index=False)


# Criar o gráfico
plt.figure(figsize=(12, 6))
plt.bar(chuva_diaria['Data'], chuva_diaria['Precipitação (mm)'], width=0.2, color='dodgerblue')
plt.title('Chuva Diária - Junho 2023')
plt.xlabel('Data')
plt.ylabel('Precipitação (mm)')
plt.xticks(chuva_diaria['Data'], rotation=90, ha='right')
plt.grid(False)
plt.tight_layout()
# Exibir o gráfico

plt.show()