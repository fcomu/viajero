from math import *
lista = []
lista2 = []
resultado = 0
abeja = []

def Buscar(lista2, x):
    i = 0
    while (1):
        if lista2[i] == x:
            lista2.pop(i)
        i = i + 1

def Lectura():
    i=0
    archivo = open("archivo.txt", "r")
    lineasarch = (len(open("archivo.txt").readlines())-2)
    for linea in archivo.readlines():
        if i > 5 and i <= lineasarch:
            cadena = linea.split()
            ejex = float(cadena[1])
            ejey = float(cadena[2])
            dis = sqrt((ejex**2)+(ejey**2))
            lista.append(dis)
            lista2.append(dis)
        i = i + 1

def llenarabeja():
    i = 0
    while i < 5:
        abeja.append(1)
        i = i + 1

"""
B = numero de abeja en el panal
NC = numeros de pasos constructivos en forwars pass
"""
def BCO():
        
    
        
Lectura()
lista2.pop(0)
llenarabeja()
BCO()
