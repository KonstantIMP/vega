from string import ascii_uppercase as letters, digits
from flask import Flask, request, jsonify
from os import path
import json

import nn

app = Flask(__name__)

@app.route('/verify', methods=["POST"])
def get_img() :
    file = request.files['image']

    face_img = open('face.jpg', 'wb+')
    face_img.write(file.read())
    face_img.close()

    name = nn.get_name('face.jpg', 'keras_model.h5', 'labels.txt')

    if name == False :
        return jsonify({'status': 'error'})
    print(name)

    return jsonify({'msg': 'success'})

if __name__ == "__main__":
    print('[DEBUG] Server is starting...')

    if not path.exists('config.json') or path.isdir('config.json'):
        def_cfg = {'db_name': 'mos_ru', 'db_host': '127.0.0.1',
                   'db_user': 'root', 'db_password': 'passwd',
                   'server_port': '5003', 'kb_nn' : 'keras_model.h5',
                   'kb_desc' : 'labels.txt'}

        with open('config.json', 'w') as cfg_file:
            json.dump(def_cfg, cfg_file)

        print('[WARNING] config.json can\'t be found. Using default config')

    with open('config.json', 'r') as cfg_file:
        data = json.load(cfg_file)

    print('[DEBUG] Config was loaded :')
    print('\tDatabase name      : ' + data['db_name'])
    print('\tDatabase host      : ' + data['db_host'])
    print('\tDatabase user      : ' + data['db_user'])
    print('\tDatabase password  : ' + ('*' * len(data['db_password'])))
    print('\tServer port        : ' + data['server_port'])

    app.run(port=data['server_port'])
