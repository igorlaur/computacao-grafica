arquivo: ac5.py
import numpy as np
import cv2

def bola (img, cor):
    cv2.circle(img, (130, 230), 50, cor, -1)

def ret (imagem, cor):
    cv2.rectangle(img, (10, 50), (100, 200), cor, -1)