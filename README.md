## 📚  Descrição 

API que recebe uma imagem em formato HTTP , processa no openCV  e retorna a imagem com os rostos de pessoas marcados com um quadrado no em um link https .
## 📌Endpoints:

Foi criado apenas um endpoint do tipo POST onde é passado o link da imagem:

### /identifyfaces

Retorna a imagem processada em outro link https.

![image](https://user-images.githubusercontent.com/18649504/73939587-904f5a00-48c8-11ea-98d0-bb270cbea793.png)

## 🚀 Tecnologias Usadas 

<img src="https://user-images.githubusercontent.com/18649504/66262823-725cd600-e7be-11e9-9cea-ea14305079db.png" width = "100">

<img src="https://user-images.githubusercontent.com/18649504/73895529-a58f9e80-485e-11ea-8705-7d2e7881b814.png" width = "100">

## 📌 Estrutura do Projeto 
    |-- main.py
    |-- processImage.py
    |-- imgApi.py
    |-- haarcascade_frontalface_default.xml
    |-- requirements.txt
    |-- APIOpenCV.postman_collection.json
    
main.py -> Arquivo principal , que roda a API
<br>
processImage.py -> Classe que processa a imagem e retorna em base64 com os rostos destacados
<br>
imgApi.py -> Classe que faz o upload da imagem na internet e retorna o link https da mesma
<br>
haarcascade_frontalface_default.xml -> arquivo de referência de classificação da imagem do openCV
<br>
requirements.txt -> Bibliotecas utilizadas
<br>
APIOpenCV.postman_collection.json -> Arquivo de importação para teste no postman
<br>

## 📢 Como executar

Requisitos:

Python 3.7.4<br>

Instalar todas as depedências do python usando o arquivo requiriments.txt que está no projeto:  

```bash 
pip install  -r requirements.txt
 ```  
 Executar o main.py no cmd com o comando:

```bash 
python main.py
 ```  
Para efetuar o teste você precisa somente utilizar algum programa que consiga fazer um post na API REST( Recomendo o Postman que de sugestão já deixei a collection dentro do arquivo do projeto).

```bash 
APIOpenCV.postman_collection.json
 ```  
e informar o IP: http://127.0.0.1:5000/+endpoint , preenchendo o body no formato JSON conforme abaixo:

![image](https://user-images.githubusercontent.com/18649504/73939759-e7edc580-48c8-11ea-8cb4-e39d5eb708a9.png)


## 🔓 Licença 
MIT © [Paulo Mota](https://www.linkedin.com/in/paulo-mota-955218a2/)
