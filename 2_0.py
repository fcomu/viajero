import math
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

def Lectura(): #maneja la lectura del archivo
    i=0
    archivo = open("archivo.txt", "r")
    lineasarch = (len(open("archivo.txt").readlines())-2)
    for linea in archivo.readlines():
        if i > 5 and i <= lineasarch:
            cadena = linea.split()
            ejex = float(cadena[1]) #obtenemos eje x
            ejey = float(cadena[2]) #obtenemos eje y
            dis = math.sqrt((ejex**2)+(ejey**2)) #se calcula un tipo de hipotenuza para el nodo
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
        a = randint(1, 30) #le damos valores random a las abejas entre 1 y 30
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
    dist = 0.0 #valor para tener valor de las distancias
    aux = 0.0
    aux_lista = lista 
    global NC 
    while i in range(0, len(lista)): #manejo de fila
        while j in range(0, len(lista2)):  #manejo de columna
            dist = math.fabs(float(lista[i]) - float(lista2[j])) #calcula distancias
            if aux == 0 or aux < dist: #compruba nuevo aux de distancia
                aux = dist
            if aux > dist: #si auxilia es mayo se le pasa el menor
                aux = dist
                recorrido.append(k) #al recorrido le dara el nodo por los que pasa
                NC = NC + 1
                lista2.pop(j)
            j = j + 1
            k = k + 1
        aux_lista.pop(i)
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
    randomabeja() #inicializa abeja 
    k=0
    iniciarnodo()
    while True:
        k = k + 1 
        mover()
        if k <= NC: #verifica condicion de verdad para BCO
            break
        return BCO


def sumar():
    i = 0
    valor = 0 
    while i in range(0, len(recorrido)): #ciclo para hacer el recorrido
        valor = valor + recorrido[i] #es el resultado 
        i = i + 1 #maneja el recorrido
    print valor #imprime el valor despues del los saltos por los nodo
    
Lectura() #lee la informacion de los archivos de texto
lista2 = lista #se igualan las listas
lista2.pop(0) #saca primer elemento de la seguna lista
llenarabeja()   #llena las abjeas con numero random
BCO() #algoritmo abeja
sumar() #suma todo los nodos
