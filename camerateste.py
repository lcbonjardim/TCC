import numpy as np
import cv2
import face_recognition as fr
from engine import reconhece_face, get_rostos

import img as img

video_capture = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
file = "./img/desconhecido_atual.jpg"  # gera a foto da camera
while True:
    ret, img = video_capture.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30,30)
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x,y),(x+w,y+h), (0,255,255),2)
    cv2.imshow('TCC Reconhecimento', img)


    if cv2.waitKey(1)& 0xFF == ord('s'):
        cv2.imwrite(file,img)
        break

cv2.destroyAllWindows()

desconhecido = reconhece_face("./img/desconhecido_atual.jpg")
if (desconhecido[0]):
    rosto_desconhecido = desconhecido[1][0]
    rostos_conhecidos, nomes_dos_rostos = get_rostos()
    resultados = fr.compare_faces(rostos_conhecidos, rosto_desconhecido)
    print(resultados)

    # Verifica dentro de um range de rostos conhecidos se existe alguem igual
    for i in range(len(rostos_conhecidos)):
        resultado = resultados[i]
        if (resultado):
            print("Rosto do", nomes_dos_rostos[i], "foi reconhecido")
        # Se não tem ninguem igual ele devolve a mensagem que não encontrou nenhum rosto conhecido
        else:
            if i == len(rostos_conhecidos) and resultado == False:
                print("Nao foi encontrado nenhum rosto")


