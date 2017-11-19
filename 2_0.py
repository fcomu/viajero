from math import *
from random import randint

lista = []
lista2 = []
resultado = 0
abeja = []
camino = []
recorrido = []
NC = 0

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
        i = i + 1

def llenarabeja():
    i = 0
    while i < 5:
        abeja.append(1)
        i = i + 1


def randomabeja():
    i = 0
    while i < 5:
        a = randint(1, 30)
        print a
        camino.append(a)        
        i = i + 1

def iniciarnodo():
    i = 0
    j = 0
    while i < 5 :
        while j in lista2:
            if lista2[j] != camino[0] and lista2[j] != camino[1] and lista2[j] != camino[2] and lista2[j] != camino[3] and lista2[j] and camino[4]:
                lista2.pop(j) 
            j = j + 1
        i = i + 1

def mover():
    i = 0
    j = 0
    k = 0
    dist = 0.0
    aux = 0.0
    while lista[i] <= len(lista):
        while lista2[j] <= len(lista2):
            dist = abs(lista[i] - lista2[j])
            if aux == 0:
                aux = dist
            
            if aux > dist:
                aux = dist
                recorrido.append(k)
                NC = NC + 1
                lista2.pop(j)
                break;
            j = j + 1
            k = k + 1
        i = i + 1
             

"""
definiciones
B = numero de abeja en el panal (trabajando con 5)
NC = numeros de pasos constructivos en forwars pass
1ra parte
1 inciar soluciones vacias para cada aveja
2 cada abeja:
    a) k = 1
    b) evaluar todos los movimientos
    c) escojer utilizando ruleta
    d) k++
    e) si k <= NC ir a (b)
3) todas las abejas regresan (backward pass)
4) evaluar solucion parcial
5) abeja sigue o cambia solucion se convierte reclutadora o seguidora
6) seguidora va con reclutadora
7) solucion no completa ir paso 2
8) evaluar todas las solucion
9) si no es cumplida condicion termino ir paso 2
10) mostrar mejor solucion
"""
def BCO():
    randomabeja()  
    k=0
    iniciarnodo()
    while True:
        k = k + 1
        mover()
        if k <= NC:
            break
        return BCO



        
Lectura()
lista2 = lista
llenarabeja()
BCO()
print recorrido[1]
