import json


class JSON_files():
    base = 'base.json'
    product = 'product.json'
    users = 'users.json'
    orders = 'orders.json'


class Base():
    name_json_file = JSON_files.base

    def load_data(self):
        with open(self.name_json_file) as file:
            data = json.load(file)

        return data

    def dump_data(self, data):
        with open(self.name_json_file, 'w') as file:
            json.dump(data, file, indent=4)

    def update(self, *keys, **namekeys):

        data = self.load_data()

        if len(keys) == 1:
            data.setdefault(keys[0], {})
        elif len(keys) == 2:
            data.setdefault(keys[0], {}).setdefault(keys[1], {})
            if len(namekeys) == 1:
                data[keys[0]][keys[1]] = namekeys['value']
        elif len(keys) == 3:
            data.setdefault(keys[0], {}).setdefault(keys[1], {}).setdefault(keys[2], {})
            if len(namekeys) == 1:
                data[keys[0]][keys[1]][keys[2]] = namekeys['value']

        self.dump_data(data)

        return 'Данные успешно обновлены.'

    def value_for_key(self, key):
        data = self.load_data()
        return data.get(key, 'Такого ключа нет.')


class User(Base):
    name_json_file = JSON_files.users

    def login(self):
        data = self.load_data()
        while True:
            log = input('Введите Логин: ')
            if log not in data:
                return log
            else:
                print('Введите логин заново. Такой уже есть.')
                continue

class Product(Base):
    name_json_file = JSON_files.product


