import os.path
import json

class Config :
    def __init__(self, cfg_name='vega.json') :
        self.debug_mode = False
        self.db_addr = '0.0.0.0'
        self.cfg_file = cfg_name

        if os.path.isfile(cfg_name) == False : self.__write_changes()
        else :
            with open(cfg_name, 'r') as f :
                data = json.load(f)

                if 'debug' in data : self.debug_mode = data['debug']
                if 'db_addr' in data : self.db_addr = data['db_addr']

                self.__write_changes()

    def __write_changes(self) :
        def_rec = {
            'debug' : self.debug_mode,
            'db_addr' : self.db_addr
        }

        with open(self.cfg_file, 'w+') as f :
            json.dump(def_rec, f)

    def get_debug(self) : return self.debug_mode

    def get_db_addr(self) : return self.db_addr

    def set_debug(self, d_value) :
        self.debug_mode = d_value
        self.__write_changes()

    def set_db_addr(self, addr_value) :
        self.db_addr = addr_value
        self.__write_changes()
