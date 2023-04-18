import cv2
import numpy as np

# Processeo padrão =======================================================
# lendo a imagem que vamos trabalhar
img = cv2.imread('assets/fotos/cats.jpg')
cv2.imshow('Cats', img)

# desenhando um canva branco do mesmo tamanho que a imagem de trabalho
blank = np.zeros(img.shape, dtype='uint8')
# cv2.imshow('Blank', blank)

# transferindo-a para cinza
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('Gray', gray)

# Detecção de contornos ==================================================
# Primeiro devemos borrar a imagem, com a função GaussianBlur ja ensinada em aulas passadas
# Lembrando que quanto maior o valor de ksize (5,5) maior o blur
blur = cv2.GaussianBlur(gray, (5,5), cv2.BORDER_DEFAULT)
# cv2.imshow('Blur', blur)

# Usando a função canny para detecção de bordas, como ensinado anteriormente é uma função muito padrão para detecção de bordas;
# Funciona detectando descontinuidades no brilho.
canny = cv2.Canny(blur, 125, 175)
# cv2.imshow('Canny Edges', canny)

'''
A novidade dessa aula começa aqui:
Para detectar os contornos de uma imagem, é recomendado até pela própria biblioteca:
"For better accuracy, use binary images. So before finding contours, apply threshold or canny edge detection."

cv2.findContours(imagem, modo_deteccao, metodo_aproximacao_contorno)

Modo de Detecção:
Recomendo a utilização de cv2.RETR_LIST, é o recomendado pela documentação

Métodos de Aproximação de Contorno:
Os contornos são os limites de uma forma com a mesma intensidade na imagem. 
Ele armazena as coordenadas (x,y) do limite de uma forma. Mas ele armazena todas as coordenadas? Isso é especificado por este método de aproximação de contorno.
cv.CHAIN_APPROX_NONE: salva absolutamente todos os pontos de contorno, custoso, imagina se tivessemos uma linha apenas, precisamos de todos os pontos ou apenas seus dois extremos?
cv.CHAIN_APPROX_SIMPLE: Ele remove todos os pontos redundantes e comprime o contorno, economizando memória.
Há um exemplo nos assets/didaticas que mostra duas imagens, na primeira precisamos de 734 pontos para detectar o contorno, na segunda apenas 4, somente variando os métodos
'''

contours, hierarchies = cv2.findContours(canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
# contours, hierarchies = cv2.findContours(canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
print(f'{len(contours)} contornos encontrados!!')

cv2.drawContours(blank, contours, -1, (0,0,255), 1)
cv2.imshow('contornos desenhados', blank)

cv2.waitKey(0)