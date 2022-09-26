from matriz_mezclada import *
from copy import deepcopy

import random


def encontrar_cero_anchura(matrizMezclada):
    #encontrar posicion 0
    #matriz mezclada = matriz original
    for fila in range(len(matrizMezclada)):
        for columna in range(len(matrizMezclada)):
            if matrizMezclada[fila][columna]==0:
                #print (f"EL 0 esta en la posicion ({fila},{columna})".format(fila, columna))
                return fila, columna
                

def posiciones_anchura(matriz):

    matriz_original = matriz
    posFilaCero, posColCero= encontrar_cero(matriz_original)  #posFilaCero=fila donnde esta el cero y posColCero=columna donde esta el cero    
    mixedMatriz= [posFilaCero, posColCero]

    
        
#print("matriz")
#----FILA1----
#00
    if mixedMatriz == [0,0]:
        movimientos=[1,2]
        r = random.choice(movimientos)
        if r == 1:
            matriz_original[0][0], matriz_original[0][1] = matriz_original[0][1], matriz_original[0][0] 
        else:
            matriz_original[0][0], matriz_original[1][0] = matriz_original[1][0], matriz_original[0][0]
            
#01
    elif mixedMatriz == [0,1]:
        movimientos=[1,2,3]
        r = random.choice(movimientos)
        if r == 1:
            matriz_original[0][1], matriz_original[0][0] = matriz_original[0][0], matriz_original[0][1] 
        
        elif r == 2:
            matriz_original[0][1], matriz_original[0][2] = matriz_original[0][2], matriz_original[0][1] 
        
        else:
            matriz_original[0][1], matriz_original[1][1] = matriz_original[1][1], matriz_original[0][1]
        
#02
    elif mixedMatriz == [0,2]:
        movimientos=[1,2]
        r = random.choice(movimientos)
        if r == 1:
            matriz_original[0][2], matriz_original[0][1] = matriz_original[0][1], matriz_original[0][2] 
        
        else:
            matriz_original[0][2], matriz_original[1][2] = matriz_original[1][2], matriz_original[0][2]
        
#----FILA2----
#10
    elif mixedMatriz == [1,0]:
        movimientos=[1,2,3]
        r = random.choice(movimientos)
        if r == 1:
            matriz_original[1][0], matriz_original[0][1] = matriz_original[0][1], matriz_original[1][0] 
        
        elif r == 2:
            matriz_original[1][0], matriz_original[2][0] = matriz_original[2][0], matriz_original[1][0] 
        
        else:
            matriz_original[1][0], matriz_original[1][1] = matriz_original[1][1], matriz_original[1][0]
        
#11
    elif mixedMatriz == [1,1]:
        movimientos=[1,2,3,4]
        r = random.choice(movimientos)
        if r == 1:
            matriz_original[1][1], matriz_original[0][1] = matriz_original[0][1], matriz_original[1][1]
        
        elif r == 2:
            matriz_original[1][1], matriz_original[2][1] = matriz_original[2][1], matriz_original[1][1]
        
        elif r == 3:
            matriz_original[1][1], matriz_original[1][2] = matriz_original[1][2], matriz_original[1][1]
        
        else:
            matriz_original[1][1], matriz_original[1][0] = matriz_original[1][0], matriz_original[1][1]
        
#12
    elif mixedMatriz == [1,2]:
        movimientos=[1,2,3]
        r = random.choice(movimientos)
        if r == 1:
            matriz_original[1][2], matriz_original[0][2] = matriz_original[0][2], matriz_original[1][2] 
        
        elif r == 2:
            matriz_original[1][2], matriz_original[2][2] = matriz_original[2][2], matriz_original[1][2] 
        
        else:
            matriz_original[1][2], matriz_original[1][1] = matriz_original[1][1], matriz_original[1][2]
        
# ----FILA3----
# 20
    elif mixedMatriz == [2,0]:
        movimientos=[1,2]
        r = random.choice(movimientos)
        if r == 1:
            matriz_original[2][0], matriz_original[2][1] = matriz_original[2][1], matriz_original[2][0] 
        
        else:
            matriz_original[2][0], matriz_original[1][0] = matriz_original[1][0], matriz_original[2][0]
        
#21
    elif mixedMatriz == [2,1]:
        movimientos=[1,2,3]
        r = random.choice(movimientos)
        if r == 1:
            matriz_original[2][1], matriz_original[2][0] = matriz_original[2][0], matriz_original[2][1] 
        
        elif r == 2:
            matriz_original[2][1], matriz_original[2][2] = matriz_original[2][2], matriz_original[2][1] 
        
        else:
            matriz_original[2][1], matriz_original[1][1] = matriz_original[1][1], matriz_original[2][1]
        
#22
    elif mixedMatriz == [2,2]: 
        movimientos=[1,2]
        r = random.choice(movimientos)
        if r == 1:
            matriz_original[2][2], matriz_original[2][1] = matriz_original[2][1], matriz_original[2][2] 
        
        else:
            matriz_original[2][2], matriz_original[1][2] = matriz_original[1][2], matriz_original[2][2]
    return matriz_original

def busquedaNiveles(matrizAnchura, matrizOriginal):
    niveles = []
    contador = 0
    matriz = deepcopy(matrizAnchura)
    #matriz = []
    while True:
        a = posiciones(matriz)
        contador += 1
        for i in a:
            niveles.append(i)
            matriz = deepcopy(matriz)
        if a == matrizOriginal:
            print(f"Encontraste la solucion en {contador} movimientos!!\n", a)
            break

            
        
        


    



    



