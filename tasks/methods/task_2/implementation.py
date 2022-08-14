class MyException(Exception):
    pass


class ClassFather:
    childs = []

    @classmethod
    def register(cls):
        if cls == ClassFather:
            raise MyException
        cls.childs.append(cls)

    @classmethod
    def get_name(cls):
        if cls == ClassFather:
            raise MyException
        elif cls in cls.childs:
            return cls._name
        else:
            raise MyException

class User1(ClassFather):
    _name = 'user1'


class User2(ClassFather):
    _name = 'user2'

class_father = ClassFather()
first_child = User1()
second_child = User2()


first_child.register()
print(first_child.get_name())