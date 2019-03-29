import cv2
import numpy as np   

def retangulo(nome):
	imagem = np.zeros((200, 300, 3), dtype = "uint8")
		
	for y in range(0, imagem.shape[0]):
			for x in range(0, imagem.shape[1]):
				imagem[y, x] = (255,0,0)
	
	cv2.imshow(nome, imagem)
	cv2.waitKey(0) 

retangulo("teste")