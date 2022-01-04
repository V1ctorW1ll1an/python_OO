class Writer:
    def __init__(self, nome):
        self.__name = nome
        self.__tool = None

    @property
    def name(self):
        return self.__name

    @property
    def tool(self):
        return self.__tool

    @tool.setter
    def tool(self, value):
        self.__tool = value


class Pen:
    def __init__(self, brand):
        self.__brand = brand

    @property
    def brand(self):
        return self.__brand

    def writing(self):
        print("pen is writing")


class Typewriter:
    def writing(self):
        print('typewriter is writing')
