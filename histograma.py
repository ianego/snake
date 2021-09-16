# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 14:34:48 2021

@author: ricky
"""

"from matplotlib import pyplot as plt"
"import matplotlib.ticker as ticker"

def lectura_texto():
    archivo_texto = open('GEH.txt', 'r')
    texto = archivo_texto.readlines()
    archivo_texto.close()
    return texto

def separacion_texto(texto):
    palabras = []
    renglon = []
    i = 0
    while i < len(texto):
        if (texto[i] == '\n'):
            texto.remove('\n')
            i-=1
        i+=1
    
    for i in range(len(texto)):
        linea = texto[i].replace("\n", "")
        renglon.append(linea)
    for j in range(len(renglon)):
        palabra = renglon[j].split(" ")
        palabras = palabras + palabra
    return palabras

def lista_palabras(palabras):
    palabra = []

    for i in range(len(palabras)):
        palabra_actual = palabras[i]
        for j in range(len(palabras)):
            if palabra_actual not in palabra :
                palabra.append(palabras[i])
    
    return palabra

def contador_palabras(texto_separado,palabras):
    num_palabras = []
    
    for i in range(len(palabras)):
        num_veces = 0;
        for j in range(len(texto_separado)):
            if (palabras[i]==texto_separado[j]):
                num_veces = num_veces + 1
        num_palabras.append(num_veces)
    
    return num_palabras
        
texto = lectura_texto()
texto_separado = separacion_texto(texto)
palabras = lista_palabras(texto_separado)
num_palabras = contador_palabras(texto_separado, palabras)
print(num_palabras)