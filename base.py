import json


class JSON_files():
    base = 'base.json'
    product = 'product.json'
    users = 'users.json'
    orders = 'orders.json'


class Base():

    def load_data(self, name_json):
        with open(name_json) as file:
            data = json.load(file)

        return data

    def dump_data(self, data, name_json):
        with open(name_json, 'w') as file:
            json.dump(data, file, indent=4)

    def update(self, *keys, **namekeys):

        data = self.load_data(JSON_files.base)

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

        self.dump_data(data, JSON_files.base)

        return 'Данные успешно обновлены.'

    def value_for_key(self, key):
        data = self.load_data(JSON_files.base)
        return data.get(key, 'Такого ключа нет.')


item = Base()

print(item.value_for_key('Dany'))

