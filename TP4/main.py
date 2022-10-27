from MultiLayerPerceptron4 import *
from mlp import *
def main():
    cantCO = int(input("Cantidad de neuronas para la capa oculta: "))
    #capaOculta = MultiLayerPerceptron().crearNeuronaCO(cantCO)
    #print(capaOculta)
    #iteraciones = int(input("Cantidad de iteraciones: "))
    #MultiLayerPerceptron().perceptronCO(capaOculta, iteraciones)
    capaOculta = MultiLayerPerceptron2().crearNeuronaCO(cantCO)
    pCO = MultiLayerPerceptron2().capaOculta(capaOculta)
    pCF=MultiLayerPerceptron2().capaFinal(pCO, cantCO)
    MultiLayerPerceptron2().nuevosValores(capaOculta,pCF)
if __name__ == '__main__':
    main()
