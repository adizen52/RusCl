import json
import validators
import datetime
from UsersCl import User
def load_json_users():
    with open('users.json') as users:
       file  = json.load(users)
    return file

def dump_json_users(file):
    with open('users.json', 'w') as users:
        json.dump(file, users, indent=4)
def enter(data):
    while True:
        name = input('Введите логин для входа: ')
        if name not in data:
           print('Такого логина нет.')
           continue
        password = input('Введите пароль: ')
        if password != data[name]['password']:
            print('Не верныый пароль, повторите вход!')
            continue
        print('Вы успешно вошли в учетную запись.')
        return name


def user_login(data):
    while True:
        login = input('Введите Ваш логин для регистрации: ')
        if login in data:
            print('Такой логин уже существует. Введите другой.')
            continue
        else:
            return login

def user_email(data):
    while True:
        us_email = input('введите вашу почту: ')
        if validators.email(us_email, whitelist = None):
            flag = 0
            for i in data:
                if data[i]['email'] == us_email:
                    flag = 1
                    break
            if flag == 1:
                print('Такой емаил уже существует, введите другой: ')
            else:
                return us_email
        else:
            print('Неверный формат EMAIL. Введите заново.')
            continue



def hb_date():
    hb = input('Введите Вашу дату рождения в формате: YYYY-MM-DD: ')
    try:
        datetime.date.fromisoformat(hb)
        return hb
    except ValueError:
        print('Не правильный ввод даты. Повторите попытку.')
        return hb_date()


def add_user_obj(name):
    user = User.get(name)
    return user