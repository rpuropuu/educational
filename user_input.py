#def reverse(text):
#    return text[::-1]


#def is_palindrome(text):
#    return text == text[::-1]


text = input('Введите текст: ')

if (text == text[::-1]):
    print('Да, это палиндром')
else:
    print('Нет, это не палиндром')
