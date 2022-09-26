from matriz import *
from matriz_mezclada import *
from busqueda_random import *
from busqueda_anchura import *

def main():
    cont=int(input("Cuantas veces quiere mezclar la matriz: "))
    matriz1 = crear_matriz()
    print(f"MATRIZ ORIGINAL:\n {matriz1} ")
    matrizOriginal = crear_matriz()
    #print (matriz1)
    matriz2= encontrar_cero(matriz1)
    matriz3 = posiciones(matriz1)
    #print (matriz3)
    matrizMez = matrizDesordenada(matriz1, cont)
    print("BUSQUEDA RANDOM")
    matrizRandom = busquedaRandom(matrizMez, matrizOriginal)
    print("BUSQUEDA EN ANCHURA")
    #matrizAnchura1 =  encontrar_cero_anchura(matrizMez)
    matrizAnchura2 = posiciones_anchura(matrizMez)

    matrizAnchura3 = busquedaNiveles(matrizAnchura2, matrizOriginal)



if __name__ == '__main__':
    main()
