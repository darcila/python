from random import randrange
from time import sleep

matriz = []
longitudx = 10
longitudy = 10

#Creamos la función que recibe 2 parametros X y Y
def crear_matriz(x=0,y=0):

    for i in range(x):
        matriz.append([])
        for j in range(y):
            matriz[i].append(None)


def imprimir_matriz():
    longitud = len(matriz)
    for i in range(longitud):
        print(matriz[i])

def llenar_izquierda():
    for i in range(longitudx):
        matriz[i][i] = randrange(100)
        sleep(1)
        imprimir_matriz()


crear_matriz(longitudx, longitudy)
llenar_izquierda()
