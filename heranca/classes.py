class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.class_name = self.__class__.__name__


class Client(People):
    pass


class Student(People):
    pass
