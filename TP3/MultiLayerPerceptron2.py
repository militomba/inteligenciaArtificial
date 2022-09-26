import math
class MultiLayerPerceptron():
    def perceptron(self):
        
        entrada0 = 1
        entrada1 = 0
        entrada2 = 0
        SalidaDeseada = 0
        lr = 0.1

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

        #NEURONA 1
        x1= (w0*entrada0) + (w1*entrada1) + (w2*entrada2) 
        y1 = 1 / (1 + (math.exp(-x1)))
        error1 = SalidaDeseada - y1
        delta1 = y1*(1-y1)*error1

        deltaw0 = lr*entrada0*delta1
        w0 = w0 + deltaw0
    
        deltaw1 = lr*entrada1*delta1
        w1 = w1 + deltaw1
       
        deltaw2 = lr*entrada2*delta1
        w2 = w2 + deltaw2

        print(f"---NEURONA 1---\nSalida Real={y1} \nw0={w0}\nw1={w1}\nw2={w2}")
        
        #NEURONA 2
        x2= (w3*entrada0) + (w4*entrada1) + (w4*entrada2) 
        y2 = 1 / (1 + (math.exp(-x2)))
        error2 = SalidaDeseada - y2
        delta2 = y2*(1-y2)*error2

        deltaw3=lr*entrada0*delta2
        w3=w3 + deltaw3

        deltaw4=lr*entrada1*delta2
        w4=w4 + deltaw4

        deltaw5=lr*entrada0*delta2
        w5=w5 + deltaw5

        print(f"\n---NEURONA 2---\nSalida Real={y2} \nw3={w3}\nw4={w4}\nw5={w5}")

        #NEURONA 3
        x3= (w6*entrada0 + w7*entrada1 + w8*entrada2) 
        y3 = 1 / (1 + (math.exp(-x3)))
        error3 = SalidaDeseada - y3
        delta3 = y3*(1-y3)*error3

        deltaw6 = lr*entrada0*delta3
        w6= w6 + deltaw6

        deltaw7 = lr*y1*delta3
        w7= w7 + deltaw7

        deltaw8 = lr*y2*delta3
        w8= w8 + deltaw8

        print(f"\n---NEURONA 3---\nSalida Real={y3} \nw6={w6}\nw7={w7}\nw8={w8}")

        #NEURONA 4
        x4= (w9*entrada0 + w10*y1 + w11*y2 + w12*y3)
        y4 = 1 / (1 + (math.exp(-x4)))
        error4 = SalidaDeseada - y4
        delta4 = y4*(1-y4)*error4

        deltaw9 = lr * entrada0*delta4
        w9 = w9 - deltaw9

        deltaw10 = lr *y1*delta4
        w10 = w10 - deltaw10

        deltaw11 = lr *y2*delta4
        w11 = w11 - deltaw11

        deltaw12 = lr *y3*delta4
        w12 = w12 - deltaw12

        print(f"\n---NEURONA 4---\nSalida Real={y4}\nx={x4} \nw9={w9}\nw10={w10}\nw11={w11}\nw12={w12}")
if __name__ == '__main__':
    MultiLayerPerceptron().perceptron()