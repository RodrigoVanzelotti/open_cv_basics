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

