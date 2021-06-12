def func(str_1, str_2):
    count = 0
    try:
        if len(str_1) == 10 and len(str_2) == 10:
            for i, j in zip(str_1, str_2):
                if i == j:
                    count += 1
                else:
                    continue
            print(f'Строки совпадают на {count * 10} %')
        else:
            print('Строки дожны быть длинной в 10 букв или символов')
    except TypeError:
        print('Аргументы должны быть в строковом типе')

func('asdfghjklo', 'qseftgjukl')
func('helloworld', 'helloworld')
