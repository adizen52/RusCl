import json

class Base():
    def update(self, *keys, **namekeys):
        with open('base.json') as data:
            file_json = json.load(data)

        if len(keys) == 1:
            file_json.setdefault(keys[0], {})
        elif len(keys) == 2:
            file_json.setdefault(keys[0], {}).setdefault(keys[1], {})
            if len(namekeys) == 1:
                file_json[keys[0]][keys[1]] = namekeys['value']
        elif len(keys) == 3:
            file_json.setdefault(keys[0], {}).setdefault(keys[1], {}).setdefault(keys[2], {})
            if len(namekeys) == 1:
                file_json[keys[0]][keys[1]][keys[2]] = namekeys['value']

        with open('base.json', 'w') as data:
            json.dump(file_json, data, indent= 4)

        return 'Данные успешно обновлены.'

item = Base()

item.update('Dany', 'Addres', value='Nizniy Novgorod, Lenina, 3')
item.update('Dany', 'Age', value=27)
item.update('Dany', 'Car', value={'Marka': 'Porshe',
                                  'Model': 'Cayen'})
item.update('Dany', 'Car', 'Corobka', value='Robot')
item.update('Dany', 'Age', value=24)
item.update('Robby', 'Dany', value=15)
item.update('Mariska', 'Age', value=32)
item.update('Maroon', 'Age', value=18)
item.update('Maroon', 'Address', value={'country' : 'Russia',
                                        'city' : 'Moscow',
                                        'street' : 'Lenina',
                                        'house' : '2'})
print(item.update('Maroon', 'Address', 'city', value='SPB'))