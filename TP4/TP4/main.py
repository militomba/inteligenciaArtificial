from distutils.dir_util import copy_tree
import random
from capaOculta import *
from capaFinal import *
import matplotlib.pyplot as plt
def main():
    tabla_xor1 = [[0, 0, 0],[0, 1, 1],[1, 0, 1],[1, 1, 0]] 
    tabla_xor2 = [[1,0, 0, 0],[1,0, 1, 1],[1,1, 0, 1],[1,1, 1, 0]] 

    cantCO = int(input("Cantidad de neuronas para la capa oculta: "))
    cantPesos= cantCO*3 

    #LISTAS
    listaPesosCO = []
    listaPesosCF = []
    listaSalidaReal = []
    contador = []
    
    listaError1 = []
    listaError2 = []
    listaError3 = []
    listaError4 = []

    #pesos capa oculta
    for j in range(cantPesos):
        r = random.uniform(-1.0,1.0)
        redondeado = round(r,ndigits=4)
        listaPesosCO.append(redondeado)
    division = [listaPesosCO[i:i+3] for i in range(0, len(listaPesosCO), 3)]
    print(f"PESOS CAPA OCULTA: {division}")

    #pesos capa final
    for i in range (cantCO+1):
        rCF = random.uniform(-1.0,1.0)
        redondeadoCF = round(rCF,ndigits=4)
        listaPesosCF.append(redondeadoCF)
    print(f"PESOS CAPA FINAL: {listaPesosCF}")

    iteraciones = 0
    
    while iteraciones != 10000:
        iteraciones += 1
        contador.append(iteraciones)
        print(f"----------------------ITERACION N°{iteraciones}----------------------")
        for fila in tabla_xor2:
            
            cortada = fila [0:3]
            sd = fila[3]
            for capaoculta in division:
                salidaRealCO = CapaOculta().neuronaCapaOculta(cortada, capaoculta)
                listaSalidaReal.append(salidaRealCO)
            deltaFinal, nuevosValores, error = CapaFinal().neuronaCapaFinal(listaSalidaReal, listaPesosCF, sd)                           
            listaPesosCF.clear()
            listaPesosCF = nuevosValores   
            if fila == tabla_xor2[0]:
                listaError1.append(error)
            elif fila == tabla_xor2[1]:
                listaError2.append(error)
            elif fila == tabla_xor2[2]:
                listaError3.append(error)
            elif fila == tabla_xor2[3]:
                listaError4.append(error)

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
            division = [nuevosPesosCO[i:i+3] for i in range(0, len(nuevosPesosCO), 3)]
            

    fig, ax = plt.subplots()
    ax.plot(contador, listaError1, label="Error fila 1")
    ax.plot(contador, listaError2, label="Error fila 2")
    ax.plot(contador, listaError3, label="Error fila 3")
    ax.plot(contador, listaError4, label="Error fila 4")
    ax.set_xlabel("ITERACIONES", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:green'})
    ax.set_ylabel("ERRORES", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:blue'})
    plt.title("Error en base de las iteracion")
    plt.legend()
    plt.savefig('grafigoErroresEnBaseIteracion')
    plt.show()

  
                 
        

        
       
        


        
        
                

        
        
            
            

if __name__ == '__main__':
    main()