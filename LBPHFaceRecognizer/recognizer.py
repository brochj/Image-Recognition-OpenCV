# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 12:06:21 2018

@author: broch
"""

import cv2 
import numpy as np

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml') # arquivo que foi gerado pelo trainer.py baseado no dataset das pessoas que quero reconhecer
cascadePath = "haarcascade_frontalface_default.xml" #arquivo treinado para recocenher faces frontais
faceCascade = cv2.CascadeClassifier(cascadePath);

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0) #inicia camtura da câmer

while True: #quando chegar ao milésimo frame, para
    ret, frame = cam.read()

    #frame não pode ser obtido? entao sair
    if(ret == False):
        cam.release()
        break
    

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    #se nenhuma face for achada, continue
    #if not np.any(faces):  # com isso trava quando nao detecta nenhum rosto
     #   continue

    rostos = []
    #achou uma face? recorte ela (crop)
    for (x, y, w, h) in faces:
        rosto = frame[y:y+h, x:x+w]
        #esse rosto é grande o bastante pra ser levado
        #em conta
        if(((x + w) - x) > 100 and ((y + h) - y) > 100):

            #modifica o tamanho dele pra se ajustar ao
            #treinamento e pinte pra tons de cinza
            rosto = cv2.resize(rosto, (255, 255))
            rosto = cv2.cvtColor(rosto, cv2.COLOR_BGR2GRAY)

            #aqui ele recebe a foto e diz qual rótulo
            #pertence (ou seja, quem é)
            label = recognizer.predict(rosto)
            font = cv2.FONT_HERSHEY_SIMPLEX
            if(label[0] == 0): #é o broch?
                #então bota um texto em cima da caixinha
                cv2.putText(frame,'Broch',(x - 20,y + h + 60), font, 2.5,(255,0,0),5,cv2.LINE_AA)
                #pinte um retângulo ao redor do rosto do broch
                frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            if(label[0] == 1): #é a obama?
                #então bota um texto em cima da caixinha
                cv2.putText(frame,'Not Bad',(x - 20,y + h + 60), font, 1.5,(0,0,255),5,cv2.LINE_AA)
                #pinte um retângulo ao redor do rosto 
                frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)

    #redimensione só pra ficar bonito na tela
    frame = cv2.resize(frame, (int(0.75 * frame.shape[1]), int(0.75 * frame.shape[0])))

    #exibir na tela!
    cv2.imshow("reconhecimento", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
