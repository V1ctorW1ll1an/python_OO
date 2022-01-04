

class BaseDeDados:
    def __init__(self):
        self.__dados = {}
        self.dados_publicos = {}
        self._dados_protegidos = {}
    
    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_clientes(self, id):
        del self.__dados['clientes'][id]

    @property
    def dados(self):
        return self.__dados

    @dados.setter
    def dados(self, novo_valor):
        self.__dados = novo_valor