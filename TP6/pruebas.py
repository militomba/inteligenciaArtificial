from distutils.dir_util import copy_tree
import random
from capaOculta import *
from capaFinal import *
import matplotlib.pyplot as plt
from leerImagenes import *
import numpy as np

def pruebas():
    iteraciones = 0
    contador = []
    tabla_imagen = leer_imagenes()
    cantCO = int(input("Cantidad de neuronas para la capa oculta: "))
    entradas = len(tabla_imagen[0])-1 #7681 entradas
    entradasCO = cantCO* entradas

    listaPesosCO = []
    listaPesosCF = []
    

    for i in range(entradasCO):
        rCO = random.uniform(-0.01, 0.01)
        listaPesosCO.append(rCO)
    
    division = [listaPesosCO[i:i+entradas] for i in range(0, len(listaPesosCO), entradas)] #[[7681], [7681],...]

    for i in range(cantCO+1):
        rCF = random.uniform(-0.01, 0.01)
        listaPesosCF.append(rCF) 

    
    for i in tabla_imagen:
        j = i[:-1]
        a = len(j)
        for d in division:
            c = len(d)
            mult = np.multiply(j, d)
            print(mult)
            

    print(f"CANTIDAD DE ENTRASAS: {a}\nCANTIDAD DE PESOS: {c}")

if __name__ == '__main__':
    pruebas()