# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 00:34:27 2023

@author: nepor
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
estanqueidadeCompleta = pd.read_csv('D:\Codigos_VSCODE\Programas_didaticos_Python\dataframe_estanqueidade_poco_BUZ12valvula_aberta2022-12.csv')

#Tudo para Buzz 12
dataframeDownstreamPressureDez2022 = estanqueidadeCompleta.iloc[:352, 4:8].values

eixoY = dataframeDownstreamPressureDez2022[:,2]
eixoX = dataframeDownstreamPressureDez2022[:,1]
fonte1 = {'family':'serif','color':'blue','size':20}
fonte2 = {'family':'serif','color':'darkred','size':15}

plt.plot(eixoX,eixoY)
plt.title("Estanqueidade Main_Data_DownstreamProductionPressure_Value Dez 2022", fonte1)
plt.xlabel("Timestamp", fonte2)
plt.ylabel("Valor de pressão", fonte2)
plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)


dataframeUpstreamPressureDez2022 = estanqueidadeCompleta.iloc[:352, 8:12].values
eixoY1 = dataframeUpstreamPressureDez2022[:,2]
eixoX1 = dataframeUpstreamPressureDez2022[:,1]

plt.plot(eixoX1,eixoY1)
plt.title("Estanqueidade Main_Data_UpstreamProductionPressure_Value Dez 2022", fonte1)
plt.xlabel("Timestamp", fonte2)
plt.ylabel("Valor de pressão", fonte2)
plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)



#Jan 2023

estanqueidadeCompleta1 = pd.read_csv('D:\Codigos_VSCODE\Programas_didaticos_Python\dataframe_estanqueidade_poco_BUZ12valvula_aberta2023-01.csv')

dataframeDownstreamPressureJan2023 = estanqueidadeCompleta1.iloc[:323, 4:8].values

eixoY2 = dataframeDownstreamPressureJan2023[:,2]
eixoX2 = dataframeDownstreamPressureJan2023[:,1]

plt.plot(eixoX2,eixoY2)
plt.title("Estanqueidade Main_Data_DownstreamProductionPressure_Value Jan 2023", fonte1)
plt.xlabel("Timestamp", fonte2)
plt.ylabel("Valor de pressão", fonte2)
plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)

dataframeUpstreamPressureJan2023 = estanqueidadeCompleta1.iloc[:323, 8:12].values

eixoY3 = dataframeUpstreamPressureJan2023[:,2]
eixoX3 = dataframeUpstreamPressureJan2023[:,1]

plt.plot(eixoX3,eixoY3)
plt.title("Estanqueidade Main_Data_UpstreamProductionPressure_Value Jan 2023", fonte1)
plt.xlabel("Timestamp", fonte2)
plt.ylabel("Valor de pressão", fonte2)
plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)



#Fevereiro 2023

estanqueidadeCompleta2 = pd.read_csv('D:\Codigos_VSCODE\Programas_didaticos_Python\dataframe_estanqueidade_poco_BUZ12valvula_aberta2023-02.csv')

dataframeDownstreamPressureFev2023 = estanqueidadeCompleta2.iloc[:342, 4:8].values

eixoY4 = dataframeDownstreamPressureFev2023[:,2]
eixoX4 = dataframeDownstreamPressureFev2023[:,1]

plt.plot(eixoX4,eixoY4)
plt.title("Estanqueidade Main_Data_DownstreamProductionPressure_Value Fev 2023", fonte1)
plt.xlabel("Timestamp", fonte2)
plt.ylabel("Valor de pressão", fonte2)
plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)

dataframeUpstreamPressureFev2023 = estanqueidadeCompleta2.iloc[:33, 8:12].values

eixoY5 = dataframeUpstreamPressureFev2023[:,2]
eixoX5 = dataframeUpstreamPressureFev2023[:,1]

plt.plot(eixoX5,eixoY5)
plt.title("Estanqueidade Main_Data_UpstreamProductionPressure_Value Fev 2023", fonte1)
plt.xlabel("Timestamp", fonte2)
plt.ylabel("Valor de pressão", fonte2)
plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)

#Marco 2023

estanqueidadeCompleta3 = pd.read_csv('D:\Codigos_VSCODE\Programas_didaticos_Python\dataframe_estanqueidade_poco_BUZ12valvula_aberta2023-03.csv')

dataframeDownstreamPressureMar2023 = estanqueidadeCompleta3.iloc[:574, 4:8].values

eixoY6 = dataframeDownstreamPressureMar2023[:,2]
eixoX6 = dataframeDownstreamPressureMar2023[:,1]

plt.plot(eixoX6,eixoY6)
plt.title("Estanqueidade Main_Data_DownstreamProductionPressure_Value Mar 2023", fonte1)
plt.xlabel("Timestamp", fonte2)
plt.ylabel("Valor de pressão", fonte2)
plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)

dataframeUpstreamPressureMar2023 = estanqueidadeCompleta3.iloc[:574, 8:12].values

eixoY7 = dataframeUpstreamPressureMar2023[:,2]
eixoX7 = dataframeUpstreamPressureMar2023[:,1]

plt.plot(eixoX7,eixoY7)
plt.title("Estanqueidade Main_Data_UpstreamProductionPressure_Value Mar 2023", fonte1)
plt.xlabel("Timestamp", fonte2)
plt.ylabel("Valor de pressão", fonte2)
plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)

#Aberturas e fechamentos de valvulas



aberturasDez2022 = pd.read_csv('D:\Codigos_VSCODE\Programas_didaticos_Python\dataframe_momento_valvulas_poco_BUZ12valvula_aberta2022-12.csv')
aberturasJan2023 = pd.read_csv('D:\Codigos_VSCODE\Programas_didaticos_Python\dataframe_momento_valvulas_poco_BUZ12valvula_aberta2023-01.csv')
aberturasFev2023 = pd.read_csv('D:\Codigos_VSCODE\Programas_didaticos_Python\dataframe_momento_valvulas_poco_BUZ12valvula_aberta2023-02.csv')
aberturasMar2023 = pd.read_csv('D:\Codigos_VSCODE\Programas_didaticos_Python\dataframe_momento_valvulas_poco_BUZ12valvula_aberta2023-03.csv')

relatoriosValvulasDez2022 = pd.read_csv('D:\Codigos_VSCODE\Programas_didaticos_Python\dataframe_relatorio_valvulas_BUZ122022-12.csv')
relatoriosValvulasJan2023 = pd.read_csv('D:\Codigos_VSCODE\Programas_didaticos_Python\dataframe_relatorio_valvulas_BUZ122023-01.csv')
relatoriosValvulasFev2023 = pd.read_csv('D:\Codigos_VSCODE\Programas_didaticos_Python\dataframe_relatorio_valvulas_BUZ122023-03.csv')
relatoriosValvulasMar2023 = pd.read_csv('D:\Codigos_VSCODE\Programas_didaticos_Python\dataframe_relatorio_valvulas_BUZ122023-03.csv')

