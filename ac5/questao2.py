import numpy as np
import cv2

def retangulo(nome, largura, altura , cor):
	imagem = np.zeros((altura, largura, 3), dtype = "uint8")
		
	for y in range(0, imagem.shape[0]):
			for x in range(0, imagem.shape[1]):
				imagem[y, x] = cor

	cv2.imshow(nome, imagem)
	cv2.waitKey(0) 

retangulo("teste", 50,100,(100,100,0))