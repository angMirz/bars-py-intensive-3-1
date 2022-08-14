class Coffee:
    def __init__(self, ingridients, name="Coffee"):
        self.ingridients = ingridients
        self.name = name

    @classmethod
    def make_capucino(cls, ingridients):
        return cls(ingridients, "Capucino")
    
    @classmethod
    def make_latte(cls, ingridients):
        return cls(ingridients, "Latte")

    @classmethod
    def make_glasse(cls, ingridients):
        return cls(ingridients, "Glasse")

capucino = Coffee.make_capucino(['milk'])
glasse = Coffee.make_glasse(['milk', 'chocolate'])
latte = Coffee.make_latte(['milk', 'sugar'])

print(capucino.ingridients, capucino.name)
print(glasse.ingridients, glasse.name)
print(latte.ingridients, latte.name)
