class Pizza:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    @classmethod
    def margarita(cls):
        name = 'Margarita'
        ingredients = ['mozarella', 'tomatos', 'olives']
        return cls(name, ingredients)

    @staticmethod
    def calculate_area(radius):
        pi = 3.14
        return pi * radius ** 2

marg = Pizza.margarita()
print(marg.name)
print(marg.ingredients)
print(marg.calculate_area(radius=50))
