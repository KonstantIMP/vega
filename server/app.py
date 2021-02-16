from string import ascii_uppercase as letters, digits
from flask import Flask, request, jsonify
from os import path
import json

app = Flask(__name__)

@app.route('/verify', methods=["POST"])
def get_img() :
    file = request.files['image']

    print(file.name)

    return jsonify({'msg': 'success'})

if __name__ == "__main__":
    print('[DEBUG] Server is starting...')

    if not path.exists('config.json') or path.isdir('config.json'):
        def_cfg = {'db_name': 'mos_ru', 'db_host': '127.0.0.1',
                   'db_user': 'root', 'db_password': 'passwd',
                   'server_port': '5003'}

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
