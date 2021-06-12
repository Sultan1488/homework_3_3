class Person:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(f'My name is {self.name}')


def func(*args):
    for i in args:
        try:
            i.show_name()
        except AttributeError:
            print('У данного аргумента нет имени')
    return ''

john = Person('John')
alice = Person('Alice')
charlie = Person('Charlie')

func(john, alice, charlie)
