import math
import numpy as np
class CapaOculta():
    def neuronaCapaOculta(self,filaXOR, listaPesos ):
        x = np.multiply(filaXOR, listaPesos)
        sumatoria = sum(x)
        salidaReal = 1 / (1 + (np.exp(-sumatoria)))
        #print(f"Salida real {salidaReal}")
        return salidaReal 
   
 
        
        
        
