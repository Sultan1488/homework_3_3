import random


def decorator(func):
    def wrapper():
        def func(times):
            for i in range(times):
                random_num = random.randrange(1, 101)
                print(f'Ваше случайное число - {random_num}')
            return f'Функция отработала {i + 1} раз'
        return func(7)
    return wrapper
