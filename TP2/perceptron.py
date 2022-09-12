from cProfile import label
import math
import matplotlib.pyplot as plt

class Perceptron():
    def perceptron(self):
        tabla_or = [[0, 0, 0],[0, 1, 1],[1, 0, 1],[1, 1, 1]]
        tabla_and = [[0,0,0], [0,1,0],[1,0,0],[1,1,1]]
        tabla_xor = [[0,0,0],[0,1,1],[1,0,1],[1,1,0]]

        #listas
        lista_w0 = []
        lista_w1 = []
        lista_w2 = []

        errorFila1 = []
        errorFila2 = []
        errorFila3 = []
        errorFila4 = []

        listacontador = []
        listacontadorpeso = []

        w0=0.9
        w1=0.66
        w2=-0.2

        error=1

        

        
        print("Opciones de tablas para trabajar: \n1)Tabla OR \n2)Tabla AND \n3)Tabla XOR")
        pregunta = (int(input("¿Quiere usar la opcion 1, 2 o 3?", )))
        if pregunta == 1:
            tabla = tabla_or
            print ("\nTABLA OR")
            for i in tabla:
                print(i)
        elif pregunta == 2:
            tabla = tabla_and
            print ("\nTABLA AND")
            for j in tabla:
                print(j)
        elif pregunta == 3:
            tabla = tabla_xor
            print ("\nTABLA XOR")
            for k in tabla:
                print(k)
        else:
            print("Esa no es una opcion")
        
        print(f"\n---DATOS--- \nw0 = {w0} \nw1 = {w1} \nw2 = {w2} \nerror = {error}")

        contador = 0
        contador_peso = 0
        while error > 0.1:
            contador +=1
            listacontador.append(contador)
            for fila in tabla:
                contador_peso +=1
                e = 1
                e1 = fila[0]
                e2 = fila[1]
                sd = fila[2] #solucion deseada
                x = (w0 * e) + (w1 * e1) + (w2 * e2)
                y = 1 / (1 + (math.exp(-x))) #solucion real
                error = sd - y #error = solucion deseada - solucion real
                delta = y*(1-y)* error
                lr = 0.1

                delta_w0 = lr * e * delta
                w0 = w0 + delta_w0
                lista_w0.append(w0)

                delta_w1 = lr * e1 * delta
                w1 = w1 + delta_w1
                lista_w1.append(w1)

                delta_w2 = lr * e2 * delta
                w2 = w2 + delta_w2
                lista_w2.append(w2)

                if fila == tabla[0]:
                    errorFila1.append(error)
                elif fila == tabla[1]:
                    errorFila2.append(error)
                elif fila == tabla[2]:
                    errorFila3.append(error)
                elif fila == tabla[3]:
                    errorFila4.append(error)
                listacontadorpeso.append(contador_peso)

        print(f"En la iteracion {contador} el error es menor al 10%")
            #print(f"\nw0 = {w0} \nw1 = {w1} \nw2 = {w2} \nError = {error}")

        #GRAFICOS
        #peso en base a las iteraciones
        print("IMPRIMIENDO GRAFICOS")
        fig, ax = plt.subplots()
        ax.plot(listacontadorpeso, lista_w0, label="w0")
        ax.plot(listacontadorpeso, lista_w1, label="w1")
        ax.plot(listacontadorpeso, lista_w2, label="w2")
        plt.title("Peso en base de las iteracion")
        plt.legend()
        plt.savefig('grafigoPesoEnBaseIteracion')
        plt.show()
        #errores en base a las iteraciones
        fig, er = plt.subplots()
        er.plot(listacontador, errorFila1, label="Error fila 1")
        er.plot(listacontador, errorFila2, label="Error fila 2")
        er.plot(listacontador, errorFila3, label="Error fila 3")
        er.plot(listacontador, errorFila4, label="Error fila 4")
        plt.title("Error en base de las iteracion")
        plt.legend()
        plt.savefig('grafigoErrorEnBaseIteracion')
        plt.show()        




        

        

     

if __name__ == '__main__':
    Perceptron().perceptron()