import cv2
import numpy as np

cap = cv2.VideoCapture('assets/videos/dog.mp4')
# Utilizamos resize e rescale para ganhar espaço e não perder qualidade de um vídeo/imagem

# Vamos aplicar o rescale em cada frame individualmente de um vídeo (podendo aplicar a uma imagem)
# Utilizando um função
def rescale_frame(frame: np.array,
                 scale: float = 0.75):
    # image, video, livevideo
    largura = int(frame.shape[1] * scale)
    altura = int(frame.shape[0] * scale)

    # cv2.INTER_AREA é só uma maneira que o cv2 tem de interpolar para calcular como vai tratar os pixels no resize
    return cv2.resize(frame, (largura, altura), interpolation=cv2.INTER_AREA)

# Função que muda a resolução
def resize_frame(width: int,
                 height: int):
    # só função pra livevideo
    cap.set(3, width)
    cap.set(4, height)
# é possível aplicar o processo em imagens e vídeos

# IMAGEM =====================================
# img = cv2.imread('assets/fotos/cat.jpg')

# resized_image = rescale_frame(img, 0.2)
# cv2.imshow('resized_cat', resized_image)
# cv2.waitKey(0)

# VIDEO ======================================
# Ler vídeos é um pouquinho diferente de ler imagens, pois temos que ler frame a frame de um vídeo
# Pra isso criamos um loop que opera sobre a função .read() do objeto cap (que é o VideoCapture)
while True:
    # confirmacao, frame = cap.read()
    _, frame = cap.read()

    frame_resize = rescale_frame(frame, 0.2)

    # cv2.imshow('video do dog', frame)
    cv2.imshow('video do dog', frame_resize)
    
    if cv2.waitKey(20) & 0xFF==ord('q'):
        break

