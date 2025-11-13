from datetime import datetime

while True:
    inp = input("Введите дату или команду выхода(q):")
    if inp == 'q':
        break
    try:
        print(datetime.strptime(inp, '%A, %B %m, %Y'))
    except ValueError as e:
        try:
            print(datetime.strptime(inp, '%A, %d.%m.%y'))
        except ValueError as e:
            try:
                print(datetime.strptime(inp, '%A, %d %B %Y'))
            except ValueError as e:
                continue
