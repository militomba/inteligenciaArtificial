import math
import matplotlib.pyplot as plt
class MultiLayerPerceptron():
    def perceptron(self, iteracion):
        tabla_xor = [[0,0,0],[0,1,1],[1,0,1],[1,1,0]]

        #lr = 0.1
        lr =0.5
        #NEURONA1
        w0=0.9
        w1=0.7
        w2=0.5
        #NEURONA2
        w3=0.3
        w4=-0.9
        w5=-1
        #NEURONA3
        w6=0.8
        w7=0.35
        w8=0.1
        #NEURONA4
        w9=-0.23
        w10=-0.79
        w11=0.56
        w12=0.6
        iter = iteracion
        
        #listas
        errorFila1 = []
        errorFila2 = []
        errorFila3 = []
        errorFila4 = []

        listacontadorerror = []
        listacontadorpeso = []

        lista_w0 = []
        lista_w1 = []
        lista_w2 = []
        lista_w3 = []
        lista_w4 = []
        lista_w5 = []
        lista_w6 = []
        lista_w7 = []
        lista_w8 = []
        lista_w9 = []
        lista_w10 = []
        lista_w11= []
        lista_w12= []
        n = 0
        m = 0
        for i in range(iter):
            
            print(f"\n---ITERACION: {i}---")
            m+=1
            f=0
            listacontadorerror.append(m)
            for fila in tabla_xor:
                n +=1
                f+= 1
                print(f"\n---FILA N°{f} DE LA TABLA XOR---")
                entrada0=1
                entrada1 = fila[0]
                entrada2 = fila[1]
                SalidaDeseada = fila[2]
                #NEURONA 1
                x1= (w0*entrada0) + (w1*entrada1) + (w2*entrada2) 
                y1 = 1 / (1 + (math.exp(-x1)))

                
                print(f"\n---NEURONA 1---\nPesos: {w0},{w1},{w2}\nSalida Real={y1}\nx={x1}")
                #NEURONA 2
                x2= (w3*entrada0) + (w4*entrada1) + (w4*entrada2) 
                y2 = 1 / (1 + (math.exp(-x2)))
                
                print(f"\n---NEURONA 2---\nPesos: {w3},{w4},{w5}\nSalida Real={y2}\nx={x2}")
                #NEURONA 3
                x3= (w6*entrada0 + w7*entrada1 + w8*entrada2) 
                y3 = 1 / (1 + (math.exp(-x3)))

                print(f"\n---NEURONA 3---\nSalida Real={y3} ")
                #NEURONA 4
                x4= (w9*entrada0 + w10*y1 + w11*y2 + w12*y3)
                y4 = 1 / (1 + (math.exp(-x4)))
                error4 = SalidaDeseada - y4
                delta4 = y4*(1-y4)*error4

                deltaw9 = lr * entrada0*delta4
                nw9 = w9+deltaw9
                w9 = nw9
                lista_w9.append(nw9)

                deltaw10 = lr *y1*delta4
                nw10 = w10 + deltaw10
                w10 = nw10
                lista_w10.append(nw10)

                deltaw11 = lr *y2*delta4
                nw11 = w11 + deltaw11
                w11 = nw11
                lista_w11.append(nw11)

                deltaw12 = lr *y3*delta4
                nw12 = w12 + deltaw12    
                w12 = nw12 
                lista_w12.append(nw12)
                print(f"\n---NEURONA 4---\nSalida Real={y4}\nx4={x4}")

                #agregar errores a la lista
                if fila == tabla_xor[0]:
                    errorFila1.append(error4)
                elif fila == tabla_xor[1]:
                    errorFila2.append(error4)
                elif fila == tabla_xor[2]:
                    errorFila3.append(error4)
                elif fila == tabla_xor[3]:
                    errorFila4.append(error4)

            #-----REGLA DELTA----
                #print("\n---REGLA DELTA---\nDeltas de mi Capa Oculta para Neuronas 1, 2 y 3")
                deltafinal = delta4
                #---NEURONA 1---
                dco1 = y1*(1-y1)*deltafinal
                deltaw0 = lr * entrada0 * dco1
                dw0 = w0 +deltaw0
                w0 = dw0
                lista_w0.append(dw0)
                deltaw1 = lr * entrada1 * dco1
                dw1 = w1 +deltaw1
                w1 = dw1
                lista_w1.append(dw1)
                deltaw2 = lr * entrada2 * dco1
                dw2 = w2 +deltaw2
                w2 = dw2
                lista_w2.append(dw2)

                listacontadorpeso.append(n)

                #print(f"Neurona1\nδoc1={dco1}\nw0={dw0}\nw1={dw1}\nw2={dw2}")
                #---NEURONA 2---
                dco2 = y2*(1-y2)*deltafinal
                deltaw3 = lr * entrada0 * dco2
                dw3 = w3 +deltaw3
                w3 = dw3
                lista_w3.append(dw3)
                deltaw4 = lr * entrada1 * dco2
                dw4 = w4 +deltaw4
                w4 = dw4
                lista_w4.append(dw4)
                deltaw5 = lr * entrada2 * dco2
                dw5 = w5 +deltaw5
                w5 = dw5
                lista_w5.append(dw5)
                #print(f"Neurona2\nδoc1={dco2}\nw3={dw3}\nw4={dw4}\nw5={dw5}")
                #---NEURONA 3---
                dco3 = y3*(1-y3)*deltafinal
                deltaw6 = lr * entrada0 * dco3
                dw6 = w6 +deltaw6
                w6 = dw6
                lista_w6.append(dw6)
                deltaw7 = lr * entrada1 * dco3
                dw7 = w7+deltaw7
                w7 = dw7
                lista_w7.append(dw7)
                deltaw8 = lr * entrada2 * dco3
                dw8 = w8 +deltaw8
                w8 = dw8
                lista_w8.append(dw8)
                #print(f"Neurona3\nδoc1={dco3}\nw6={dw6}\nw7={dw7}\nw8={dw8}")

                #Graficos
                #peso en base a las iteraciones
        print("IMPRIMIENDO GRAFICOS")
        fig, ax = plt.subplots()
        ax.plot(listacontadorpeso, lista_w0, label="w0")
        ax.plot(listacontadorpeso, lista_w1, label="w1")
        ax.plot(listacontadorpeso, lista_w2, label="w2")
        ax.plot(listacontadorpeso, lista_w3, label="w3")
        ax.plot(listacontadorpeso, lista_w4, label="w4")
        ax.plot(listacontadorpeso, lista_w5, label="w5")
        ax.plot(listacontadorpeso, lista_w6, label="w6")
        ax.plot(listacontadorpeso, lista_w7, label="w7")
        ax.plot(listacontadorpeso, lista_w8, label="w8")
        ax.plot(listacontadorpeso, lista_w9, label="w9")
        ax.plot(listacontadorpeso, lista_w10, label="w10")
        ax.plot(listacontadorpeso, lista_w11, label="w11")
        ax.plot(listacontadorpeso, lista_w12, label="w12")
        ax.set_xlabel("ITERACIONES", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:green'})
        ax.set_ylabel("PESOS", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:blue'})
        plt.title("Peso en base de las iteracion")
        plt.legend()
        plt.savefig('grafigoPesoEnBaseIteracion')
        plt.show()
        #error en base a las iteraciones
        fig, er = plt.subplots()
        er.plot(listacontadorerror, errorFila1, label="Error fila 1")
        er.plot(listacontadorerror, errorFila2, label="Error fila 2")
        er.plot(listacontadorerror, errorFila3, label="Error fila 3")
        er.plot(listacontadorerror, errorFila4, label="Error fila 4")
        er.set_xlabel("ITERACIONES", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:green'})
        er.set_ylabel("ERRORES", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:blue'})
        plt.title("Error en base de las iteracion")
        plt.legend()
        plt.savefig('grafigoErrorEnBaseIteracion')
        plt.show()        

if __name__ == '__main__':
    iteracion=int(input("Cuantas iteraciones quiere? "))
    MultiLayerPerceptron().perceptron(iteracion)

            
