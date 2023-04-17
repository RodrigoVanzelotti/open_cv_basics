import cv2
import numpy as np

'''
O openCV trabalha de maneira padrão em BGR que é extremamente semelhante ao RGB, colorspace mais utilizado, a diferença é que:
No RGB temos: (Red, Green, Blue) para a representação de cada pixel na tela
No BGR invertemos as letras, logo temos: (Blue, Green, Red) para a representação de cada pixel na tela.

ColorSpaces são maneiras diferentes de representar uma mesma imagem, em espaços de cor diferentes. GrayScale é um tipo de ColorSpace também
Para representação de impressões utilizamos o CMYK (Ciano, Magenta, Amarelo, Preto), que representa a mistura dessas cores em um fundo branco,
enquanto o RGB ou BGR, representa a combinação de Vermelho, Verde e Azul em um fundo preto.

Essa aula é mais para apresentar os conceitos de colorspaces do que de fato descorrer sobre todos, mas os mais utilizados no mundo da informática são:
RGB: praticamente padrão
BGR: representado pelo OpenCV como padrão
CMYK: representação para impressões em mundo real
'''
img = cv2.imread('assets/fotos/cat.jpg')

# BGR para Grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Cinza', gray)

# BGR para HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('HSV', hsv)

# BGR para L*a*b
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
cv2.imshow('L*a*b', lab)

# BGR para RGB
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow('RGB', rgb)

# HSV para BGR
lab_bgr = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)
cv2.imshow('LAB para BGR', lab_bgr)


cv2.waitKey(0)
