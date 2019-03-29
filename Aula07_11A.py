# Importa os pacotes
import numpy as np
import cv2

#desenha todo branco
def circulo(img):
   branco = (255, 255, 255)
   cv2.circle(img, (130, 230), 50, branco, -1)
   
def retangulo(img):
   #desenha o retângulo todo vermelho
   vermelho = (0, 0, 255)
   cv2.rectangle(img, (250, 50), (10, 30), vermelho, -1)


if __name__ == "__main__":
   print("Testando o modulo")
   imagem = np.zeros((300, 400, 3), dtype = "uint8")

   circulo(imagem)
   retangulo(imagem)

   cv2.imshow("Imagem", imagem)
   cv2.waitKey(0)  



