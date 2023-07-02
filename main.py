from UsersDef import enter, user_email, user_login, hb_date, dump_json_users, add_user_obj, load_json_users
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
            name = input('введите Ваше ФИО: ')
            email = user_email(json_file)
            password = input('Введите пароль для учетной записи: ')
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

        q = input('Хотите поменять ФИО? y/n' )
        if q == 'y':
            fio = input('Введите ФИО')
            user_obj.name = fio

        print(user_obj.name)

market()