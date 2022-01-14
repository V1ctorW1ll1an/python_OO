"""
Em python tudo é um objeto: incluindo classes.
Metaclasses são as "classes" que criam classes.
Type é uma metaclasse (!!!???)
"""


class Meta(type):
    def __new__(mcs, name, bases, namespace):
        if name == 'A':
            return type.__new__(mcs, name, bases, namespace)
        return type.__new__(mcs, name, bases, namespace)
