# -*- coding: utf-8 -*-

with open('web_clients_correct.csv', 'r', encoding='utf-8') as inp, \
        open('out.txt', 'w', newline='') as result:
    inp.readline()
    clients = inp.read().strip().split('\n')
    a = []
    for client in clients:
        c = client.split(',')
        if int(c[4]) % 10 == 1:
            year = 'год'
        elif 1 < (int(c[4]) % 10) < 5:
            year = 'года'
        else:
            year = 'лет'
        sex = 'женского' if c[3] == 'female' else 'мужского'
        sovSex = 'совершила' if c[3] == 'female' else 'совершил'
        if c[1] == 'mobile':
            browser = 'мобильного'
        elif c[1] == 'laptop':
            browser = 'компьютерного'
        else:
            browser = 'планшетного'
        text = f'Пользователь {c[0]} {sex} пола, {c[4]} {year} {sovSex} покупку на {c[5]} у.е. с {browser} браузера {c[2]}.'
        if c[6] != '-':
            text += f' Регион, из которого совершалась покупка: {c[6]}.'
        a.append(text)
    for x in a:
        result.write(f'{x}\n')