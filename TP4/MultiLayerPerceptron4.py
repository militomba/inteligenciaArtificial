import math
import matplotlib.pyplot as plt
class MultiLayerPerceptron():
    def crearNeuronaCO(self,capaOculta):  
        cantPesos = capaOculta * 3
        listaPesos = [] 
        pesos = 0
        
        
        for j in range(cantPesos):
            pesos += 1
            m = float(input(f"Valor de W{pesos}: " ))
            condicion = True
            while condicion:
                if (m<-1 or m > 1):
                    print(f"-1<W{pesos}<1")
                    m = float(input(f"Valor de W{pesos}: " ))
                else:
                    listaPesos.append(m)
                    condicion = False
        
        #divido la lista de los pesos por neurona
        division = [listaPesos[i:i+3] for i in range(0, len(listaPesos), 3)] 
        #print(division)
        return (division)

    def perceptronCO(self, pesosNeuronas, iteraciones):
        tabla_xor = [[0,0,0],[0,1,1],[1,0,1],[1,1,0]]
        lr =0.5
        
        #print(pesosNeuronas[0])
        for i in range(iteraciones):
            print(f"\n----ITERACION: {i}----")
            f = 0
            
            for fila in tabla_xor:
                f+=1
                print(f"\nFILA N°{f} DE LA TABLA XOR")
                entrada0 = 1
                entrada1 = fila[0]
                entrada2 = fila[1]
                #salidaDeseada = fila[2]
                listaNeurona = []
                contador = 0
                for neuronas in pesosNeuronas:
                    print(neuronas)

                    for n in neuronas:
                       

                        #for n in neurona:
                        w0 = n[0]
                        print(w0)
                        w1 = n[0]
                        print (w1)
                        w2 = n[0]
                        print(w2)
                        x = (w0 * entrada0) + (w1 * entrada1) + (w2 * entrada2)
                        y = 1 / (1 + (math.exp(-x)))
                        listaNeurona.append(y)
                        contador += 1
                #print(listaNeurona)

                    


    



