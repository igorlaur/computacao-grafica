# Importa os pacotes
import numpy as np
import cv2
import Aula07_10A as minha_bib

imagem = np.zeros((300, 400, 3), dtype = "uint8")

minha_bib.circulo(imagem)

minha_bib.retangulo(imagem)

cv2.imshow("Imagem", imagem)
cv2.waitKey(0)   




