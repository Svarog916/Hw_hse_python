number = int(input())

if (number % 10 + number // 10 % 10 + number // 100 % 10) \
        == (number // 1000 % 10 + number // 10000 % 10 + number // 100_000 % 10):
    print("Счастливый билет")
else:
    print("Несчастливый билет")
