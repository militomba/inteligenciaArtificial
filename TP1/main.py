from matriz import *
from matriz_mezclada import *
from busqueda_random import *

def main():
    cont=int(input("Cuantas veces quiere mezclar la matriz: "))
    matriz1 = crear_matriz()
    matrizOriginal = crear_matriz()
    #print (matriz1)
    matriz2= encontrar_cero(matriz1)
    matriz3 = posiciones(matriz1)
    #print (matriz3)
    matrizMez = matrizDesordenada(matriz1, cont)
    matrizRandom = busquedaRandom(matrizMez, matrizOriginal)



if __name__ == '__main__':
    main()
