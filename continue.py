while True:
    s = input('Введите что-нибудь')
    if s == 'выход':
        break
    if len(s) < 3:
        print('Слишком мало символов')
        continue
    print('Введёная строка достаточной длины')
