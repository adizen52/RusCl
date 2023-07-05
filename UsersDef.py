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

def user_name(data):
    while True:
        name = input('Введите Ваше ФИО \n'
                     '(в случае двойного имение, фамилии или отчества пишите их через тире: ')
        if len(name.split()) != 3:
            ('ФИО должно стостоять из трех! Фамилия, имя отчество.')
            continue
        else:
            return name


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


def user_password():
    while True:
        password = input('Введите пароль: ')
        set_password = set(password)
        if len(password) < 6:
            print('Слишком короткий пароль (меньше 6). Попробуйте новый > 6.')
            continue
        elif len(set_password.intersection('1234567890')) == 0:
            print('В Вашем пароле не хватае цифр.')
            continue
        elif len(set_password.intersection('QWERTYUIOPASDFGHJKLZXCVBNMЙЦУКЕНГШЩЗХФЫВАПРОЛДЖЭЯЧСМИТЬБЮ')) == 0:
            print('В Вашем пароле не хватаем заглавных букв. Попробуйте снова.')
            continue
        else:
            return password

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


def get_data(user_obj):
    while True:
        qw = input('Хотите получить 1-login, 2-ФИО, 3-Почту,\n '
                   '4-ДР, 5-ВСЕ данные о себе (введите цифру)\n'
                   '6 - ВЫЙТИ из данного меню.: \n')
        if qw == '1':
            print(user_obj.login)
            continue
        elif qw == '2':
            print(user_obj.name)
            continue
        elif qw == '3':
            print(user_obj.email)
            continue
        elif qw == '4':
            print(user_obj.happybirthday)
            continue
        elif qw == '5':
            print(user_obj)
        elif qw == '6':
            break
        else:
            print('Введены не верные данные.')

def set_data(user_obj, json_file):
    while True:
        qw = input('Хотите изменить: 1-login, 2-ФИО, 3-Почту,\n '
                   '4-ДР, 5-пароль, 6 - ВЫЙТИ из данного меню.: \n')
        login_one = user_obj.login
        if qw == '1':
            input_login = user_login(json_file)
            user_obj.login = input_login
            print(f'Ваш логин изменен на {user_obj.login}')
        elif qw == '2':
            input_name = user_name(json_file)
            user_obj.name = input_name
            print(f'Ваше ФИО заменено на {user_obj.name}')
        elif qw == '3':
            input_email = user_email(json_file)
            user_obj.email = input_email
            print(f'Ваш email заменен на {user_obj.email}')
        elif qw == '4':
            input_hb = hb_date()
            user_obj.happybirthday = input_hb
            print(f'Ваша дата рождения изменена на {user_obj.happybirthday}')
        elif qw == '5':
            input_password = user_password()
            user_obj.password = input_password
            print(f'Ваш пароль изменен на: {user_obj.password}')
        elif qw == '6':
            break
        else:
            print('Введены не верные данные.')

        user_obj.save_data(json_file, login_one)
        continue

def delete_data(user_obj, json_file):
    while True:
        q = input('Если хотите удалить 1-ФИО, 2-почту, 3-ДР, 4-выйти из данного меню: ')
        if q == '1':
            del user_obj.name
            print('Ваше ФИО удалено')
            continue
        elif q == '2':
            del user_obj.email
            print('Ваша почта удалена')
            continue
        elif q == '3':
            del user_obj.happybirthday
            print('Ваше день рождение удалено')
            continue
        elif q == '4':
            break

        user_obj.save_data(json_file)
