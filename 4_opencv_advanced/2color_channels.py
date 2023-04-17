import cv2
import numpy as np

'''
Canais de Cor (Color Channels) são as diferentes componentes de cor que compõem uma imagem. Em geral, uma imagem é composta por três canais de cor: vermelho, verde e azul (RGB). 
Cada canal representa a intensidade da cor correspondente na imagem.

Os canais de cor são importantes na visão computacional porque muitos algoritmos e técnicas de processamento de imagem dependem da manipulação desses canais. 
Por exemplo, pode ser necessário separar ou combinar canais de cor para realçar determinados recursos de uma imagem ou remover ruído. 
Além disso, a informação dos canais de cor pode ser utilizada para segmentação de objetos, detecção de bordas, reconhecimento de padrões e outras tarefas de visão computacional.
'''

# Lendo a imagem do parque
img = cv2.imread('assets/fotos/park.jpg')
cv2.imshow('Fim de semana no Parque', img)

# Crianod uma tela branca utilizando as dimensões da nossa imagem lida
blank = np.zeros(img.shape[:2], dtype='uint8')

# Função de split do cv2, que pega uma imagem(matriz) e separa os seus channels
# Como a leitura padrão do openCV é em bgr, abrimos o retorno da função cv2.split como b, g, r para que possamos absorver esses valores.
b, g, r = cv2.split(img)

# Abrimos as imagens uma a uma em seus respectivos canais, mesclando com as matrizes de zeros para que possamos entender como seria a imagem
# somente com seus respectivos canais de cor
blue = cv2.merge([b,blank,blank])
green = cv2.merge([blank,g,blank])
red = cv2.merge([blank,blank,r])

cv2.imshow('Azul', blue)
cv2.imshow('Verde', green)
cv2.imshow('Vermelho', red)

# Notemos que, os shapes são semelhantes, a diferença é que apenas a img tem 3 canais de cor
print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

# E ao juntarmos os 3 canais de cor novamente, temos a imagem original idêntica
merged = cv2.merge([b,g,r])
cv2.imshow('Merged Image', merged)

cv2.waitKey(0)