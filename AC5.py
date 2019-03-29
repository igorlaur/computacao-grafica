import numpy as np
import cv2
import aula_uma_fita

def cria_imagem_retangular_e_circulo(nome, altura=300, largura=400, cor=(255,0,0)):
    imagem = np.zeros((altura ,largura, 3), dtype="uint8")
    
    aula_uma_fita.bola(imagem, cor)
    aula_uma_fita.ret(imagem, cor)

    cv2.imshow("imagem", imagem)
    cv2.waitKey(0)

cria_imagem_retangular_e_circulo("Teste", 300, 400, (100,100,0))