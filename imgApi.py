from imgurpython import ImgurClient

class imgApi:
    def __init__(self,client_id,client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        
       
    def authImgur(self):
        client = ImgurClient(self.client_id, self.client_secret)
        return client
    def uploadImg(self,path,client):  
        response = client.upload_from_path(path, config=None, anon=True)
        print(response['link'])
        return response['link']