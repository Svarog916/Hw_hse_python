documents = [
 {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
 {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
 {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]
directories = {
 '1': ['2207 876234', '11-2'],
 '2': ['10006'],
 '3': []
}

def p():
    print('Введите номер документа:')
    n = input()
    owner = documents[[x.get('number') for x in documents].index(str(n))]['name']
    print('Владелец документа:', owner)


def s():
    print('Введите номер документа:')
    n = input()
    shelf = max(set(i if str(n) in doc else '0' for i, doc in directories.items()))
    print(str('Документ хранится на полке: ' + shelf) if shelf != '0' else 'Документ с данным номером не существует.')


while True:
    print('Введите команду:')
    inp = input()
    if inp == 'q':
        break
    if inp == 'p':
        p()
        continue
    if inp == 's':
        s()
        continue
    print('Команда некорректна.')
