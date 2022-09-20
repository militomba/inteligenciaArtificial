from distutils.log import error
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
        #NEURONA5
        w12=0.6
        w13=-0.6
        w14=0.22
        #NEURONA6
        w15=-0.22
        w16=-0.55
        w17=0.31
        w18=-0.32
        
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
        x3= (w6*entrada0 + w7*y1 + w8*y2) 
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
        x4 = (w9*entrada0 + w10*y1 + w11*y2)
        y4 = 1 / (1 + (math.exp(-x4)))
        error4 = SalidaDeseada - y4
        delta4 = y4*(1-y4)*error4

        deltaw9 = lr*entrada0*delta4
        w9= w9 + deltaw9

        deltaw10 = lr*y1*delta4
        w10= w10 + deltaw10

        deltaw11 = lr*y2*delta4
        w11= w11 + deltaw11

        print(f"\n---NEURONA 4---\nSalida Real={y4} \nw9={w9}\nw10={w10}\nw11={w11}")

        #NEURONA 5
        x5 = (w12*entrada0 + w13*y1 + w14*y2)
        y5 = 1 / (1 + (math.exp(-x5)))
        error5 = SalidaDeseada - y5
        delta5 = y5*(1-y5)*error5

        deltaw12 = lr*entrada0*delta5
        w12= w12 + deltaw12

        deltaw13 = lr*y1*delta5
        w13= w13 + deltaw13

        deltaw14 = lr*y2*delta5
        w14= w14 + deltaw14

        print(f"\n---NEURONA 5---\nSalida Real={y5} \nw12={w12}\nw13={w13}\nw14={w14}")

        #NEURONA 6
        x6 = (w15*entrada0 + w16*y3 + w17*y4 + w18*y5)
        y6 = 1 / (1 + (math.exp(-x6)))
        error6 = SalidaDeseada - y6
        delta6 = y6*(1-y6)*error6

        deltaw15 = lr*entrada0*delta6
        w15= w15 + deltaw15

        deltaw16 = lr*y3*delta6
        w16= w16 + deltaw16

        deltaw17 = lr*y4*delta6
        w17= w17 + deltaw17

        deltaw18 = lr*y5*delta6
        w18= w18 + deltaw18

        print(f"\n---NEURONA 6---\nSalida Real={y6} \nw15={w15}\nw16={w16}\nw17={w17}\nw18={w18}")

if __name__ == '__main__':
    MultiLayerPerceptron().perceptron()




