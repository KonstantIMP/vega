from flask import jsonify
from pony import orm

class Database :
    db = orm.Database()

    class Person(db.Entity) :
        name = orm.Required(str)
        surname = orm.Required(str)
        patronymic = orm.Required(str)

        login = orm.Required(str)
        passwd = orm.Required(str)

    def __init__(self, host_address, username, passwd, db_name):
        self.db.bind(provider='mysql', user=username, password=passwd, host=host_address, database=db_name)
        self.db.generate_mapping(create_tables=True)
        orm.set_sql_debug(True)

    @orm.db_session
    def get_user(self, user_surname) :
        user = self.Person.get(surname=user_surname)

        if user : return jsonify({'status' : 'ok', 'name' : user.name, 'surname' : user.surname, 'patronymic' : user.patronymic, 'login' : user.login, 'passwd' : user.passwd})
        else : return jsonify({'status' : 'error'})

