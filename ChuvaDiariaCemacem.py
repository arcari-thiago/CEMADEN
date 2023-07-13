# -*- coding: utf-8 -*-
"""
Created on Mon May 11 16:31:29 2020

@author: ThiLau
"""

import pandas as pd

filename = "mai2022.csv" #arquivo com os dados brutos do pluviógrafo
test = pd.read_csv(filename, sep=';') #, error_bad_lines=False)
test.columns=["datas","chuva"]

#blablalba
chuva_diaria = test.groupby('datas').chuva.sum()

cdiaria = chuva_diaria.to_frame()

cdiaria2 = round(cdiaria, 2)


cdiaria2.to_csv('chuva_diaria_mai2022.csv')
