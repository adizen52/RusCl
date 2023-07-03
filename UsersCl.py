import json

class User():

    def __init__(self, login, name, email, happybirtday, password):
        self.__login = login
        self.__name = name
        self.__email = email
        self.__happyd = happybirtday
        self.__password = password

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, input_login):
        self.__login = input_login

    @login.deleter
    def login(self):
        self.__login = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, input_name):
        self.__name = input_name

    @name.deleter
    def name(self):
        self.__name = None

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, input_email):
        self.__email = input_email

    @email.deleter
    def email(self):
        self.__email = None

    @property
    def happybirthday(self):
        return self.__happyd

    @happybirthday.setter
    def happybirthday(self, input_happyd):
        self.__happyd = input_happyd

    @happybirthday.deleter
    def happybirthday(self):
        self.__happyd = None

    @property
    def password(self):
        return 'Пароль можно только поменять!'

    @password.setter
    def password(self, input_password):
        self.__password = input_password

    def __str__(self):
        return f'Ваши учтеные данные: Логин - f{self.__login},\n' \
               f'                     ФИО - f{self.name}\n' \
               f'                     email - f{self.__email}\n' \
               f'                     ДР - f{self.__happyd}'

    @staticmethod
    def get(username):
        with open('users.json') as users:
            json_file = json.load(users)
        data = json_file[username]
        return User(login=username, **data)




class Order():
    pass
