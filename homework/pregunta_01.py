# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

import zipfile
import os
import pandas as pd

def pregunta_01():
    
    archivo_zip = "files/input.zip"
    
    directorio_destino = "input"

    
    if not os.path.exists(archivo_zip):
        print(f"No se encuentra el archivo {archivo_zip}.")
        return

    with zipfile.ZipFile(archivo_zip, 'r') as archivo_comprimido:
        archivo_comprimido.extractall(directorio_destino)


pregunta_01()

directorio_salida = os.path.join('files', 'output')
if not os.path.exists(directorio_salida):
    os.makedirs(directorio_salida)

frases_prueba = []
etiquetas_prueba = []
frases_entrenamiento = []
etiquetas_entrenamiento = []

directorio_prueba = os.path.join('input', 'input', 'test')
directorio_entrenamiento = os.path.join('input', 'input', 'train')

directorios_sentimiento = ['positive', 'negative', 'neutral']

for sentimiento in directorios_sentimiento:
    ruta_sentimiento = os.path.join(directorio_prueba, sentimiento)
    
    if not os.path.exists(ruta_sentimiento):
        print(f"El directorio {ruta_sentimiento} no se encuentra.")
        continue

    for archivo in os.listdir(ruta_sentimiento):
        ruta_archivo = os.path.join(ruta_sentimiento, archivo)
        
        if os.path.isfile(ruta_archivo):
            with open(ruta_archivo, 'r', encoding='utf-8') as archivo_txt:
                frase = archivo_txt.read().strip()
                
            frases_prueba.append(frase)
            etiquetas_prueba.append(sentimiento)

for sentimiento in directorios_sentimiento:
    ruta_sentimiento = os.path.join(directorio_entrenamiento, sentimiento)
    
    if not os.path.exists(ruta_sentimiento):
        print(f"El directorio {ruta_sentimiento} no se encuentra.")
        continue

    for archivo in os.listdir(ruta_sentimiento):
        ruta_archivo = os.path.join(ruta_sentimiento, archivo)
        
        if os.path.isfile(ruta_archivo):
            with open(ruta_archivo, 'r', encoding='utf-8') as archivo_txt:
                frase = archivo_txt.read().strip()
                
            frases_entrenamiento.append(frase)
            etiquetas_entrenamiento.append(sentimiento)


data_prueba = pd.DataFrame({'phrase': frases_prueba, 'target': etiquetas_prueba})
data_entrenamiento = pd.DataFrame({'phrase': frases_entrenamiento, 'target': etiquetas_entrenamiento})

data_prueba = data_prueba.sample(frac=1, random_state=42).reset_index(drop=True)
data_entrenamiento = data_entrenamiento.sample(frac=1, random_state=42).reset_index(drop=True)

data_prueba.to_csv(os.path.join(directorio_salida, "test_dataset.csv"), index=False)
data_entrenamiento.to_csv(os.path.join(directorio_salida, "train_dataset.csv"), index=False)

print("Los archivos 'train_dataset.csv' y 'test_dataset.csv' se han generado correctamente en la carpeta 'files/output'.")
    
