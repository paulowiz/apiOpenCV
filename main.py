from flask import Flask, jsonify, request,make_response
import imgApi
import processImage
import os
import io



app = Flask(__name__)

#Default Rote
@app.route('/')
def start():
    return make_response(jsonify({'success':'Api is working '}))

# if will return error 404
@app.errorhandler(404)
def handle_404_error(_error):
    """Return a http 404 error to client"""
    return make_response(jsonify({'error': 'Route not found,'}), 404)


@app.route('/identifyFaces', methods=["POST"])
def identifyfaces():
    pi = processImage.processImage('haarcascade_frontalface_default.xml')
    array = []
    link = request.json.get('link')
    response = pi.setFaces(link)
    im = imgApi.imgApi('b75fd7f114f5f5e','2be8f5d1754bcc269c6df45d2f447bcc8c8e5cf9') 
    client= im.authImgur()
    img = im.uploadImg(response,client)
    return jsonify({'img': '%s'%img})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='127.0.0.1', port=port)