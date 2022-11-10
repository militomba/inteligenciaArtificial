import cv2
import copy as cp

def leer_imagenes():
    imagen = []
    listaImagenAuxiliar = []
    person = True
    input_images_path = "D:/Mili/Documentos/facultad/CURSADO/4ANO/segundo semestre/inteligenciaArtificial/TP7/FOTOS/"
    for i in range(6):
        img = cv2.imread(input_images_path + str(i) + ".jpg", 0)
        ret, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
        listaImagenAuxiliar.clear()
        listaImagenAuxiliar.append(int(1))
        for j in range(len(img)):
            for k in range(len(img[j])):
                px = img[j][k]
                if px == 0:
                    listaImagenAuxiliar.append(int(0))
                else:
                    listaImagenAuxiliar.append(int(1))

                 #lo divido por 255 para q no me de el error de overflow
        #Si se agrega el 0 es el ivan y si se agrega el 1 es el nahue
        #Como va cambiando de true a false en cada foto, eso hace q me cambie el valor
        if person:
            listaImagenAuxiliar.append(int(0))
            person = False
        else: 
            listaImagenAuxiliar.append(1)
            person = True
        
        imagen.append(cp.deepcopy(listaImagenAuxiliar))

    return imagen