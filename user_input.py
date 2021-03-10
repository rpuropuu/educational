import string


def ready_text(text):
    some_list = list(text)
    some_len = len(text)
    new_some = ''

    for i in range(some_len):
        if some_list[i] not in string.punctuation and some_list[i] != ' ':
            new_some += some_list[i]
    return (new_some.lower())


def reverse_text(text):
    reverse_text = ready_text(text)[::-1]
    return reverse_text


def is_palindrome(text):
    print(text)
    return ready_text(text) == reverse_text(text)


something = input('Введите текст: ')
if (is_palindrome(something)):
    print("Да, это палиндром")
else:
    print("Нет, это не палиндром")
