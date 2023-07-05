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
               f'                     ДР - f{self.__happyd}\n' \
               f'\n'

    @staticmethod
    def get(username):
        with open('users.json') as users:
            json_file = json.load(users)
        data = json_file[username]
        return User(login=username, **data)

    def save_data(self, json_file, login_one):
        data_user = {}
        data_user['name'] = self.__name
        data_user['email'] = self.__email
        data_user['happybirtday'] = self.__happyd
        data_user['password'] = self.__password
        json_file[self.__login] = json_file.pop(login_one)
        with open('users.json', 'w') as users:
            json.dump(json_file, users, indent=4)


class Product:

    def __int__(self, title, description, total, price):
        self.__title = title
        self.__description = description
        self.__total = total
        self.__price = price

class Order():
    def __init__(self, id, title, description, user):
        self.__id = id
        self.__title = title
        self.description = description
        self.user = user


