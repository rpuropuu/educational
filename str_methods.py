name = 'Swaroop' # Объект строки

if name.startswith('Swa'):
    print('Да, строка начинается на "Swa"')

if 'a' in name:
    print('Да, она содержит букву "а"')

if name.find(('war')) != -1:
    print('Да, она содержит строку "war"')

delimetr = '_*_'
mylist  = ['Бразилия', 'Россия', 'Индия', 'Китай']
print(delimetr.join(mylist))
