from distutils.dir_util import copy_tree
import random
from capaOculta import *
from capaFinal import *
import matplotlib.pyplot as plt
from leerImagenes import *
from leerPesos import *
def main():
    iteraciones = 0
    contador = []
    tabla_imagen = leer_imagenes()
    cantCO = int(input("Cantidad de neuronas para la capa oculta: "))
    entradas = len(tabla_imagen[0])-1 #7681 entradas
    print(len(tabla_imagen))
    entradasCO = cantCO* entradas
   
    pesosCapaOculta, pesosCapaFinal = leerPesos()

    division = [pesosCapaOculta[i:i+entradas] for i in range(0, len(pesosCapaOculta), entradas)] #[[7681], [7681],...]

    
    listaSalidaReal = []
    lista_errores = [ [] for i in range(len(tabla_imagen))]

    while iteraciones != 70:
        iteraciones += 1
        contadorError = 0
        contador.append(iteraciones)
        print(f"----------------------ITERACION N°{iteraciones}----------------------")
        for fila in tabla_imagen:
            cortada = fila[:-1] #posicion 0 - 7681
            salidaDeseada = fila[-1] #posicion 7682
            listaSalidaReal.append(1)
            for capaoculta in division:
                salidaRealCO = CapaOculta().neuronaCapaOculta(cortada, capaoculta) 
                listaSalidaReal.append(salidaRealCO)

            deltaFinal, nuevosValores, error = CapaFinal().neuronaCapaFinal(listaSalidaReal, pesosCapaFinal, salidaDeseada)                           
            lista_errores[contadorError].append(error) 
            contadorError += 1
            pesosCapaFinal.clear()
            pesosCapaFinal = nuevosValores 


            nuevosPesosCO = []
            lr=0.5
            for peso in range(len(division)):
                Soc_genaral =listaSalidaReal[peso]*(1-listaSalidaReal[peso])*deltaFinal   
                for c in range(len(cortada)):
                    delta_general = lr*cortada[c]*Soc_genaral
                    w_general = division[peso][c] + delta_general
                    nuevosPesosCO.append(w_general)
            listaSalidaReal.clear()
            division.clear()
            division = [nuevosPesosCO[i:i+entradas] for i in range(0, len(nuevosPesosCO), entradas)]
            
    for i in range(len(lista_errores)):
        plt.plot(contador, lista_errores[i], label = f"Error r{i}")
    plt.title("ERRORES")
    plt.legend()
    plt.show()  
    plt.savefig("grafico_errores.png")



   


        
        
                

        
        
            
            

if __name__ == '__main__':
    main()