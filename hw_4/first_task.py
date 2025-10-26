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
    owner = documents[[x.get('number') for x in documents].index(n)]['name']
    print('Владелец документа:', owner)


def s():
    return 0


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
