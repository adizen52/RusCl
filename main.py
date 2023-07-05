from UsersDef import enter, user_email, user_login, hb_date, dump_json_users, add_user_obj, load_json_users
from UsersDef import get_data, user_name, set_data, user_password, delete_data
import json

def market():
    json_file = load_json_users()

    while True:
        quest = input('Хотите войти или зарегистрироваться? Y - войти / N -регистрация: ')

        if quest.lower() == 'y':
            login = enter(json_file)
            user_obj = add_user_obj(login)
            break

        elif quest.lower() == 'n':
            login = user_login(json_file)
            name = user_name(json_file)
            email = user_email(json_file)
            password = user_password()
            happyd = hb_date()

            json_file[login] = {'name' : name,
                                'email' : email,
                                'happybirtday' : happyd,
                                'password' : password}
            dump_json_users(json_file)
            user_obj = add_user_obj(login)
            break

        else:
            print('Неправильный формат ввода.')
            continue

    while True:

        q = input('Хотите 1 - получить 2 - изменить 3 - удалить, 4 - выйти: ' )
        if q == '1':
            get_data(user_obj)
            continue
        elif q == '2':
            set_data(user_obj, json_file)
            continue
        elif q == '3':
            delete_data(user_obj, json_file)
            continue
        elif q == '4':
            break






market()