from UsersDef import enter, user_email, user_login, hb_date, dump_json_users, add_user_obj, load_json_users
from UsersDef import get_data, user_name, set_data, user_password
import json

def market():
    json_file = load_json_users()

    while True:
        quest = input('Хотите войти или зарегистрироваться? Y - войти / N -регистрация: ')

        if quest.lower() == 'y':
            login = enter(json_file)
            user_obj = add_user_obj(login)

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

        else:
            print('Неправильный формат ввода.')
            continue

        q = input('Хотите получить или изменить? y/n: ' )
        if q.lower() == 'y':
            get_data(user_obj)
        elif q.lower() == 'n':
            set_data(user_obj, json_file)



        print(user_obj.name)

market()