"""
em python todas as classes derivam de object
"""


class A:
    def __init__(self):
        """
        inicializador
        """
        pass

    def __call__(self, *args, **kwargs):
        """
        faz a classe se comportar como função
        :param args:
        :param kwargs:
        :return:
        """
        resultado = 1

        for i in args:
            resultado *= i

        return resultado
