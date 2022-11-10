import math
import numpy as np
class CapaFinal():
    def neuronaCapaFinal(self, salidaRealCO, listaPesosCF, sd):

        x = 0
        for i in range(len(listaPesosCF)):
            #print(listaPesosCF[i])
            x += (listaPesosCF[i]*salidaRealCO[i])
    
            
       
        salidaReal = 1 / (1 + (np.exp(-x)))
        error = sd - salidaReal
        deltaFinal = salidaReal*(1-salidaReal)*error

        nuevosPesos = []
        lr = 0.5
    
        
        for i in range(len(salidaRealCO)):
            delta_w2 = lr*salidaRealCO[i]*deltaFinal     
            w2 = listaPesosCF[i] + delta_w2
            nuevosPesos.append(w2)
        #print("\nNeurona 4")
        print(f"SALIDA REAL CAPA FINAL: {salidaReal}")

        return deltaFinal, nuevosPesos, error