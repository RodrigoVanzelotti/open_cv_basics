import cv2
import numpy as np

# TODO REFAZER BITWISE OPERATIONS E REVISAR MASKING

'''
O mascaramento é uma técnica comum para extrair a região de interesse (ROI - Region Of Interest). 
No openCV, é possível construir uma forma de máscara arbitrária usando a função de desenho e as Bitwise Operations.
'''

img = cv2.imread('assets/fotos/cats.jpg')
cv2.imshow('AsimoCats', img)

# tela branca (que na verdade é preta)
blank = np.zeros(img.shape[:2], dtype='uint8')
# cv2.imshow('Blank Image', blank)

# criando frmas para trabalhar acerca
circle = cv2.circle(blank.copy(), (img.shape[1]//2 + 45,img.shape[0]//2), 100, 255, -1)
rectangle = cv2.rectangle(blank.copy(), (30,30), (370,370), 255, -1)

recorte = cv2.bitwise_and(circle,rectangle)
cv2.imshow('Nosso recorte para a operacao', recorte)

masked = cv2.bitwise_and(img,img,mask=recorte)
cv2.imshow('Imagem mascarada', masked)

'''
Podemos por exemplo, realizar o processo de detecção de contornos antes de realizar a bitwise_operation para que possamos
desenhar os contornos com as cores originais da imagem, só pra praticar
Resolver na aula seguinte!
'''

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5,5), cv2.BORDER_DEFAULT)
canny = cv2.Canny(blur, 125, 175)
cv2.imshow('Canny', canny)


contours, hierarchies = cv2.findContours(canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
# contours, hierarchies = cv2.findContours(canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
print(f'{len(contours)} contornos encontrados!!')

yo = cv2.drawContours(blank, contours, -1, (0,0,255), 1)
cv2.imshow('Contornos desenhados', yo)

masked2 = cv2.bitwise_and(img,img,mask=recorte)
cv2.imshow('Imagem mascarada', masked2)

cv2.waitKey(0)

