def leerPesos():
    pesos1 = []
    pesos2 = []
    with open('pesos.txt', 'r') as pesos:
        for i in pesos:
            pesos1.append(float(i))
    with open('pesos2.txt', 'r') as pesos:
        for j in pesos:
            pesos2.append(float(j))
    return (pesos1), (pesos2)