import json

class User():


    def __init__(self, name, email, happybirtday, password):
        self._name = name
        self._email = email
        self._happybirtday = happybirtday
        self._password = password

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, x):
        if len(x.split()) < 3:
            raise ValueError('ФИО должно состоять из фамилии, имени и отчества.')
        self._name = x

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, x):
        pass

    @staticmethod
    def get(username):
        with open('users.json') as users:
            json_file = json.load(users)
        data = json_file[username]
        return User(**data)

    def __str__(self):
        pass


class Order():
    pass
