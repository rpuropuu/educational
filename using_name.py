if __name__ == '__main__':
    print('Эта программа запущена сама по себе.')
    print(__name__)
else:
    print('Меня импортировали в другой модуль.')
    print(__name__)
