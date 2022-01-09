"""
em python todas as classes derivam de object
"""


class A:
    _exists = None

    def __new__(cls, *args, **kwargs):
        """
            o primeiro inicializador
        :param args:
        :param kwargs:
        """
        if not hasattr(cls, '_exists'):
            cls._exists = object.__new__(cls)
        return cls._exists

    def __init__(self):
        """
        inicializador
        """
        print("eu sou o INIT")
