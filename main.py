from flask import Flask, jsonify, request,make_response
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
    return jsonify({'base64': '%s'%response})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='127.0.0.1', port=port)