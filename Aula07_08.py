# Importa os pacotes
import numpy as np
import cv2

#desenha circulo todo branco
def circulo(img):
   branco = (255, 255, 255)
   cv2.circle(img, (130, 230), 50, branco, -1)
   

imagem = np.zeros((300, 400, 3), dtype = "uint8")

circulo(imagem)

cv2.imshow("Imagem", imagem)
cv2.waitKey(0)   


