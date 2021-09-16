# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 14:34:48 2021

@author: ricky
"""

from matplotlib import pyplot as plt
import matplotlib.ticker as ticker

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
        renglon.append(linea.upper())
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

def graficas_palabras(palabras, num_palabras):
    
    fig, axs = plt.subplots(5, 1, figsize=(15, 15))
    
    axs[0].bar(palabras[:10],num_palabras[:10])
    axs[1].bar(palabras[10:20],num_palabras[10:20])
    axs[2].bar(palabras[20:30],num_palabras[20:30])
    axs[3].bar(palabras[30:40],num_palabras[30:40])
    axs[4].bar(palabras[40:],num_palabras[40:])
    
    fig.suptitle('Histograma "Green Eggs and Ham Word Frequency"')

def main():
    
    texto = lectura_texto()
    texto_separado = separacion_texto(texto)
    palabras = lista_palabras(texto_separado)
    num_palabras = contador_palabras(texto_separado, palabras)
    graficas_palabras(palabras, num_palabras)

main()