from matriz_mezclada import posiciones
def busquedaRandom(matrizDes, matrizOriginal):
    contador = 0
    while True:
        a = posiciones(matrizDes)
        contador += 1
        if a == matrizOriginal:
            print(f"Encontraste la solucion en {contador} movimientos!!\n", a)
            break




