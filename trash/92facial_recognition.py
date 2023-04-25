import cv2
import numpy as np
import os

'''
cv2 tem um facial recognizer builtin, é sobre isso que trabalharemos
Transformar o processo de listas em dicionários para o mapping
'''

HAAR_PATH = r'C:\Users\rodri\OneDrive\Área de Trabalho\Projetos\Asimov\Inteligencia Artificial\open_cv_basics\4_opencv_advanced\haarcascade_frontalface_default.xml'
TRAIN_PATH = r'C:\Users\rodri\OneDrive\Área de Trabalho\Projetos\Asimov\Inteligencia Artificial\open_cv_basics\assets\faces\train'


cascade_class = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# faces_dir = '..\\assets\\faces\\train'
famosos = []
for famoso in os.listdir(TRAIN_PATH):
    famosos.append(famoso)

images_cut = []
index_tags = []

def create_train():
    # vamos fazer um loop para cada famoso da lista
    for famoso in famosos:
        # para cada um deles, criamos um path padrão, de acordo como as pastas estão organizadas e coletamos seu index na lista
        path = os.path.join(TRAIN_PATH, famoso)
        index_correspondente = famosos.index(famoso)
        
        # para cada imagem na pasta deste famoso, fazemos o seguinte processo:
        for img in os.listdir(path):
            # 1. Leitura de imagem
            img_path = os.path.join(path, img)
            img_matrix = cv2.imread(img_path)
            import pdb; pdb.set_trace()
            # 2. Transformamos em P&B
            cinza = cv2.cvtColor(img_matrix, cv2.COLOR_BGR2GRAY)

            # 3. Coletar os retangulos presentes na imagem
            # Perceba que aqui estamos replicando o processo de duas aulas atrás
            retangulos = cascade_class.detectMultiScale(cinza, scaleFactor=1.1, minNeighbors=4),

            # import pdb; pdb.set_trace()
            for x, y, w, h in retangulos:
                # roi = region of interest
                faces_roi = cinza[y:y+h, x:x+w]
                # utilizando notação do numpy de matrizes para recortar o rosto

                images_cut.append(faces_roi)
                index_tags.append(index_correspondente)

create_train()

print(f'Tamanho das Imagens: {len(images_cut)}')
print(f'Tamanho dos Indexes: {len(index_tags)}')