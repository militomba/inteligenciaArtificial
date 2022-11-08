import math
import numpy as np
class CapaFinal():
    def neuronaCapaFinal(self, salidaRealCO, listaPesosCF, sd):
        # print(f"----------------------NEURONA 4----------------------\n")
        # print(f"PESOS ULTIMA NEURONA: {listaPesosCF}")
        lr = 0.5
        vias =  1
        listaPesosCortada = listaPesosCF[1:]
        listax = []
       # print(f"Lista pesos cortada capa final:{listaPesosCF}")
        
        x = listaPesosCF[0]* vias
        listax.append(x)
        for i in range(len(listaPesosCortada)):
            #print(listaPesosCortada[i])
            x2 = (listaPesosCortada[i]*salidaRealCO[i])
            listax.append(x2)
        sumatoria = sum(listax)
        salidaReal = 1 / (1 + (math.exp(-sumatoria)))
        error = sd - salidaReal
        deltaFinal = salidaReal*(1-salidaReal)*error

        nuevosPesos = []
        lr = 0.5
        vias =  1
        listaPesosCortada = listaPesosCF[1:]

        delta_w1 = lr * vias * deltaFinal
        w1 = listaPesosCF[0] + delta_w1 
        nuevosPesos.append(w1)
        
        for i in range(len(salidaRealCO)):
            delta_w2 = lr*salidaRealCO[i]*deltaFinal
            w2 = listaPesosCortada[i] + delta_w2
            nuevosPesos.append(w2)
        print("\nNeurona 4")
        print(f"SALIDA REAL CAPA FINAL: {salidaReal}")

        return deltaFinal, nuevosPesos, error