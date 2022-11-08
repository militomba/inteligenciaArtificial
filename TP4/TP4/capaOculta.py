import math
import numpy as np
class CapaOculta():
    def neuronaCapaOculta(self,filaXOR, listaPesos ):
        x = np.multiply(filaXOR, listaPesos)
        sumatoria = sum(x)
        salidaReal = 1 / (1 + (math.exp(-sumatoria)))
        return salidaReal 
   
 
        
        
        
