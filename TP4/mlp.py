import math
import matplotlib.pyplot as plt
import random
import numpy as np
class MultiLayerPerceptron2():
    def crearNeuronaCO(self,capaOculta):  
        cantPesos = capaOculta * 3
        listaPesos = [] 
        pesos = 0
        
        
        for j in range(cantPesos):
           r = random.uniform(-1.0,1.0)
           redondeado = round(r,ndigits=2)
           listaPesos.append(redondeado)
           #print (redondeado)
        
        division = [listaPesos[i:i+3] for i in range(0, len(listaPesos), 3)]
        return division
    
    def capaOculta(self, pesosNeuronas):
        print("\n----------------------------------- CAPA OCULTA -----------------------------------\n")
        tabla_xor = [[0,0,0],[0,1,1],[1,0,1],[1,1,0]]
        lr =0.5
        print(pesosNeuronas)
        listaSR = []
        
        # for i in range(iteraciones+1):
        #     print(f"\n-----ITERACION {i}-----\n")
        f = 0
        for fila in tabla_xor:
            f += 1
            print(f"---------------FILA:{f}---------------\n")
            neu= 0
            entrada0 = 1
            entrada1 = fila[0]
            entrada2 = fila[1]
            listaNeurona = []
            for neurona in pesosNeuronas:
                neu+=1
                print(f"-----NEURONA {neu}-----")
                w0 = neurona[0]
                w1 = neurona[1]
                w2 = neurona[2]
                x = (w0 * entrada0) + (w1 * entrada1) + (w2 * entrada2)
                y = 1 / (1 + (math.exp(-x)))
                listaNeurona.append(y)
                print(f"w0={w0},w1={w1},w2={w2}")
                print(f"Solucion real={y}\n")
            listaSR.append(listaNeurona)
            #print(f"Lista salidas reales de la fila {f}:\n{listaNeurona}\n")
        m = 0
        for j in listaSR:
            m += 1
            print(f"LISTA SALIDA REALES FILA {m}:\n{j}")
        return listaSR
    
    def capaFinal(self, listaNeurona, entradas):
        print("\n----------------------------------- CAPA FINAL -----------------------------------\n")
        tabla_xor = [[0,0,0],[0,1,1],[1,0,1],[1,1,0]]
        listaPesos = []
        
        for j in listaNeurona:
            j.insert(0, 1)
            print(j)

        print(f"\nCANTIDAD DE ENTRADAS: {entradas}")
        #OTORGO VALOR A LA W DE LA NEURONA 4 Q HAY QUE MULTIPLICAR POR EL VIAS
        w = random.uniform(-1.0,1.0)
        rou = round(w,ndigits=2)
        #print(f"wfinal = {rou}")
        listaPesos.append(rou)
            
        for i in range(entradas):
            r = random.uniform(-1.0,1.0)
            redondeado = round(r,ndigits=2)
            listaPesos.append(redondeado)
        print (f"LISTA PESOS: {listaPesos}")
        f = 0
        #CALCULOS
        for fila in tabla_xor:
            print(fila)
            f +=1
            print(f"\n----------- FILA {f} -----------")
            salidaDeseada = fila[2]
            #print(salidaDeseada)
            n=0
            listaSD = []
            listaDelta = []
            for e in listaNeurona:
                n+=1
                print(f"\n-------- NEURONA {n} --------")
                x = np.multiply(e, listaPesos)
                suma = sum(x)
                y = 1 / (1 + (math.exp(-suma)))
                error = salidaDeseada - y
                delta = y*(1-y)*error
                listaSD.append(y)
                listaDelta.append(delta)
                print(f"x = {suma}\nSalida real = {y}\nError = {error}\nDelta = {delta} ")

            
            

            #print (listaSD)
        return listaSD, listaPesos, listaDelta

    def nuevosValores(self, capaOculta, capaFinal):
        print("\n----------------------------------- NUEVOS VALORES -----------------------------------\n")

        listaSD, listaPesos, listaDelta = capaFinal
        print (f"LISTA SALIDA DESEADA CAPA FINAL: {listaSD}")
        print (f"LISTA PESOS CAPA FINAL: {listaPesos}")
        print(f"LISTA PESOS CAPA OCULTA: {capaOculta}")
        print(f"LISTA DELTA CAPA FINAL: {listaDelta}")
        listaCF = []
        listaCO = []
        #cambiar valores capa final
        entrada0 = 1
        lr = 0.5
        # for d in listaDelta:
        #     for p in listaPesos:
        #         p[0] = lr * entrada0 * d
        #         for s in listaSD:
        #             p = lr * s * d
        #             w = p


        



            


            

        
            

        
        
        
        
        
        
        # f = 0
        # print(listaNeurona)
        # for j in listaNeurona:
        #     f+=1
        #     print(f"FILA {f}")
        #     print(j)

                    
