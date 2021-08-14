import os
from numpy.core.records import array
import pandas as pd

#Ganado enfermo
def leer_csv_enfermo (folder_path,lista_df,names):
    names = os.listdir(folder_path)
    for i in names:   
        archivo = pd.read_csv(r'''C:\Users\ASUS\OneDrive - Universidad EAFIT\ST0245-Eafit\proyecto\datasets\csv\enfermo_csv\{}'''.format(i))
        lista_df.append(archivo)
    return (lista_df)

#Ganado sano
def leer_csv_sano (folder_path,lista_df,names):
    names = os.listdir(folder_path)
    for i in names:   
        archivo = pd.read_csv(r'''C:\Users\ASUS\OneDrive - Universidad EAFIT\ST0245-Eafit\proyecto\datasets\csv\sano_csv\{}'''.format(i))
        lista_df.append(archivo)
    return lista_df

def __main__():
    folder_path_enfermo = r'C:\Users\ASUS\OneDrive - Universidad EAFIT\ST0245-Eafit\proyecto\datasets\csv\enfermo_csv'
    folder_path_sano = r'C:\Users\ASUS\OneDrive - Universidad EAFIT\ST0245-Eafit\proyecto\datasets\csv\sano_csv'
    names = []
    files = []
    leer_csv_enfermo(folder_path_enfermo, files, names)
    leer_csv_sano(folder_path_sano, files, names)
   
__main__()

