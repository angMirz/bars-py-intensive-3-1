class Tuple:
    """
    Создает неизменяемый объект с упорядоченной структурой и методами count и index.
    При создании принимается последовательность объектов.
    """

    def __init__(self, values):
        self.values = values

    def count(self, value) -> int:
        count = 0

        for item in self.values:
            if (item == value):
                count += 1
        
        return count

    def index(self, value) -> int:
        index = 0

        for item in self.values:
            if (item == value):
                return index
            index += 1
        
        raise ValueError

    
custom_tuple = Tuple([1,6,7,8,7,9])
print(custom_tuple.index(8))
print(custom_tuple.count(7))