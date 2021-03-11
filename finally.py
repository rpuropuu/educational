import time

try:
    f = open('poem.txt')
    while True: # наш обычный сопособ читать файлы
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end='')
        time.sleep(2) # пусть поспит прога
except KeyboardInterrupt:
    print('!! Вы отменили чтение файла')
finally:
    f.close()
    print('(Очистка: закрытие файла.)')
