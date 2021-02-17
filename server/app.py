from string import ascii_uppercase as letters, digits
from flask import Flask, request, jsonify
from os import path
import json

import database
import nn

app = Flask(__name__)

db = None

@app.route('/verify', methods=["POST"])
def get_img() :
    file = request.files['image']

    face_img = open('face.jpg', 'wb+')
    face_img.write(file.read())
    face_img.close()

    with open('config.json', 'r') as cfg_file:
        data = json.load(cfg_file)

    name = nn.get_name('face.jpg', data['kb_nn'], data['kb_desc'])

    if name == False :
        return jsonify({'status': 'error'})
    
    return db.get_user(name)

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

    db = database.Database(data['db_host'], data['db_user'], data['db_password'], data['db_name'])

    app.run(port=data['server_port'])
