import cv2
import numpy as np
import os

'''
cv2 tem um facial recognizer builtin, é sobre isso que trabalharemos
Transformar o processo de listas em dicionários para o mapping
'''

cascade_class = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# features = np.load('features.npy', allow_pickle=True)
# labels = np.load('labels.npy')

faces_dir = r'../assets/faces/train'
famosos = []
for famoso in os.listdir(faces_dir):
    famosos.append(famoso)

images_cut = []
index_tags = []

def create_train():
    # vamos fazer um loop para cada famoso da lista
    for famoso in famosos:
        # para cada um deles, criamos um path padrão, de acordo como as pastas estão organizadas e coletamos seu index na lista
        path = os.path.join(faces_dir, famoso)
        index_correspondente = famosos.index(famoso)
        
        # para cada imagem na pasta deste famoso, fazemos o seguinte processo:
        for img in os.listdir(path):
            # 1. Leitura de imagem
            img_path = os.path.join(path, img)
            img_array = cv2.imread(img_path)

            # 2. Transformamos em P&B
            cinza = cv2.cvtColor(cv2.COLOR_BGR2GRAY)

            # 3. Coletar os retangulos presentes na imagem
            # Perceba que aqui estamos replicando o processo de duas aulas atrás
            retangulos = cascade_class.detectMultiScale(cinza, scaleFactor=1.1, minNeighbors=4),

            for x, y, w, h in retangulos:
                # roi = region of interest
                faces_roi = cinza[y:y+h, x:x+w]
                # utilizando notação do numpy de matrizes para recortar o rosto

                images_cut.append(faces_roi)
                index_tags.append(index_correspondente)





# famosos = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']

# face_recognizer = cv2.face.LBPHFaceRecognizer_create()
# face_recognizer.read('face_trained.yml')

# img = cv2.imread(r'../Resources\Faces\val\elton_john/1.jpg')

# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('Person', gray)

# # Detect the face in the image
# faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

# for (x,y,w,h) in faces_rect:
#     faces_roi = gray[y:y+h,x:x+w]

#     label, confidence = face_recognizer.predict(faces_roi)
#     print(f'Label = {people[label]} with a confidence of {confidence}')

#     cv2.putText(img, str(people[label]), (20,20), cv2.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=2)
#     cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

# cv2.imshow('Detected Face', img)

# cv2.waitKey(0)
