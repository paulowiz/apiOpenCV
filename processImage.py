import cv2    
import requests           
import numpy as np
import base64
from PIL import Image

class processImage:
    def __init__(self,cascade_path):
        self.cascade_path = cascade_path 
        
    
    def setFaces(self,link):
        
        clf = cv2.CascadeClassifier(self.cascade_path) #Prepara classificador
        #Ler a imagem do link 
        resp = requests.get(link)
        resp = resp.content
        #converte  a imagem para array np
        image = np.asarray(bytearray(resp), dtype="uint8")
        #Passa para o formato do openCV
        img = cv2.imdecode(image, cv2.IMREAD_COLOR)
        #Passa a imagem de colorida para gray(Que é melhor)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #Defina o tamanho e a escala das faces
        faces = clf.detectMultiScale(gray, 1.3, 10) # imagem, escala 

        #Percorre todo os pixels da imagem de acordo com a classificação e gera a imagem  marcando os rostos
        for (x, y, w, h) in faces:
            img = cv2.rectangle(img, (x, y), (x+w,y+h),(255,255,0), 2) # Desenha um retângulo
          
        im = Image.fromarray(img)
        im.save("myimg.jpeg")
        return 'myimg.jpeg'

pass   
    
    