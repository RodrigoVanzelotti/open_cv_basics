import cv2
import numpy as np

# TODO REFAZER BITWISE OPERATIONS E REVISAR MASKING

'''
O mascaramento é uma técnica comum para extrair a região de interesse (ROI - Region Of Interest). 
No openCV, é possível construir uma forma de máscara arbitrária usando a função de desenho e as Bitwise Operations.
'''

'''
Nas aulas de Bitwise Operations aprendemos que podiamos utilizar 2 imagens e manipular o resultado a partir das suas intersecções.
O que não aprendemos é que podemos utilizar essas operações com 2 imagens e uma máscara para o recorte de imagens coloridas.
Então nessa aula iremos criar uma região de interesse (a partir de uma bitwise operation entre duas formas simples) e na sequencia recortar uma imagem com essa região.
'''

img = cv2.imread('assets/fotos/cats.jpg')
# cv2.imshow('AsimoCats', img)

# tela branca (que na verdade é preta)
blank = np.zeros(img.shape[:2], dtype='uint8')
# cv2.imshow('Blank Image', blank)

# criando formas para trabalhar acerca
circle = cv2.circle(blank.copy(), (img.shape[1]//2 + 45,img.shape[0]//2), 100, 255, -1)
rectangle = cv2.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
cv2.imshow('Circulo', circle)
cv2.imshow('Retangulo', rectangle)


recorte = cv2.bitwise_and(circle, rectangle)
cv2.imshow('Nosso recorte para a operacao', recorte)

masked = cv2.bitwise_and(img, img, mask=recorte)
cv2.imshow('Imagem mascarada', masked)

'''
Podemos por exemplo, realizar o processo de detecção de contornos antes de realizar a bitwise_operation para que possamos
desenhar os contornos com as cores originais da imagem, só pra praticar
Resolver na aula seguinte!
'''

cv2.waitKey(0)
