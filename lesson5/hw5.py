def start():
    print('Выберите пункт меню, введя число: ')
    print('1 – Добавить новое слово')
    print('2 – Перевести слово')
    print('3 – Изменить значение слова')
    print('4 – Удалить слово')
    print('5 - Вывести список слов')
    print('0 – Выйти')
    return


dictonary = dict()
while True:
    start()
    n = int(input('введите пункт меню: '))
    if n == 1:
        word = input('введите слово: \n')
        tran = input('введите его перевод: \n')
        dictonary[word] = tran
    elif n == 2:
        word = input('введите слово: \n')
        if word in dictonary:
            print(word, '->', dictonary[word])
        else:
            print('такого слова в словаре нет')
    elif n == 3:
        word = input('введите слово, которое нужно заменить: \n')
        tran = input('введите его перевод: \n')
        dictonary[word] = tran
    elif n == 4:
        word = input('введите слово, которое нужно удалить: \n')
        if word in dictonary:
            dictonary.pop(word)
        else:
            print('такого слова в словаре нет')
    elif n == 5:
        print(*dictonary.keys(), sep='\n')
    else:
        break