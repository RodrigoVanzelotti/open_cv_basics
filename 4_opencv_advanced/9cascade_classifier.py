import cv2
import numpy as np

'''
Cascade Classifier: 
Um Cascade Classifier (classificador em cascata) é uma técnica usada em Visão Computacional para detecção de objetos 
em imagens. Ele funciona através da combinação de vários classificadores simples em uma estrutura em cascata, 
que é treinada para identificar características específicas do objeto de interesse.

Imagine que você queira encontrar rostos em uma imagem. O Cascade Classifier irá analisar a imagem em diferentes 
estágios, cada estágio usando um classificador diferente. Por exemplo, o primeiro estágio pode usar um classificador 
simples para detectar bordas retas que possam fazer parte do rosto, enquanto o segundo estágio pode usar um 
classificador mais complexo para identificar as características do rosto, como os olhos, nariz e boca.

Cada estágio do Cascade Classifier é projetado para rejeitar rapidamente as partes da imagem que não contêm o objeto 
de interesse. Isso é importante porque a detecção de objetos pode ser computacionalmente cara e demorada, e a maioria 
das partes da imagem não contém o objeto de interesse.

Ao combinar vários classificadores em cascata, o Cascade Classifier pode alcançar alta precisão de detecção, enquanto 
mantém o tempo de processamento baixo. Essa técnica é usada em muitas aplicações de Visão Computacional, como 
reconhecimento facial, detecção de veículos em imagens de trânsito, entre outros.

Diferença Face Recognition x Face Detection

Para essa aula é necessário baixar o haarcascade_frontalface_default.xml do link:
https://github.com/opencv/opencv/tree/master/data/haarcascades
que contém diversos modelos ja treinados para casos diferentes utilizando o método de Cascade Classifier
'''

haar_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']
# features = np.load('features.npy', allow_pickle=True)
# labels = np.load('labels.npy')

face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

img = cv2.imread(r'../Resources\Faces\val\elton_john/1.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Person', gray)

# Detect the face in the image
faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h,x:x+w]

    label, confidence = face_recognizer.predict(faces_roi)
    print(f'Label = {people[label]} with a confidence of {confidence}')

    cv2.putText(img, str(people[label]), (20,20), cv2.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=2)
    cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

cv2.imshow('Detected Face', img)

cv2.waitKey(0)
