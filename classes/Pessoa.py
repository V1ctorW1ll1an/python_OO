from random import randint

class Pessoa:
    ano_atual = 2021

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


    def mostrar_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    # métodos de classe
    @classmethod
    def factory_por_ano_nascimento(cls, nome, ano_nascimento):
        ''' 
            Cria a classe Pessoa a partir do nome e do ano de nascimento
        '''
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)


    # métodos estáticos
    @staticmethod
    def gerar_id():
        rand = randint(10000, 19999)
        return rand