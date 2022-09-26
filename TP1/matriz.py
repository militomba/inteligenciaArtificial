
def crear_matriz():
    filas = 3
    columnas = 3
    matriz_original= []
    posicionCero = 0
    for i in range(filas):
        matriz_original.append([])
        for j in range(columnas):
            posicionCero +=1
            matriz_original[i].append(posicionCero) 
    matriz_original[-1][-1] = 0
    #print (matriz_original)
    
    return matriz_original





            

