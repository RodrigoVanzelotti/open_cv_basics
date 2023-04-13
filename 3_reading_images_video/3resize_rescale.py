import cv2
import numpy as np

# Utilizamos resize e rescale para ganhar espaço e não perder qualidade de um vídeo/imagem

# Vamos aplicar o rescale em cada frame individualmente de um vídeo (podendo aplicar a uma imagem)
# Utilizando um função
def rescaleFrame(frame: np.array,
                 scale: float = 0.75):
    
    largura = frame.shape[1] * scale
    altura = frame.shape[0] * scale

    return largura, altura

cap = cv2.VideoCapture('assets/videos/dog.mp4')

# Ler vídeos é um pouquinho diferente de ler imagens, pois temos que ler frame a frame de um vídeo
# Pra isso criamos um loop que opera sobre a função .read() do objeto cap (que é o VideoCapture)
while True:
    # confirmacao, frame = cap.read()
    _, frame = cap.read()

    cv2.imshow('video do dog', frame)

    # Não é necessário focar nessa explicação MAS:
    # cv2.waitKey() retorna um 32 Bit integer (pode depender da plataforma). 
    # O key input (input do teclado) é um ASCII de 8 Bit integer value. Então tu só precisa se preocupar com esses 8, os outros podem ser zero. 
    # 0xFF é uma máscara pros 8bits finais
    # é uma bitwise operation
    # É possível alcançar isso com:
    if cv2.waitKey(20) & 0xFF==ord('d'):
        break

