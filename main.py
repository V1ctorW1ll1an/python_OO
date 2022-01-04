from classes.Produto import Produto
from classes.Clientes import BaseDeDados

if __name__ =="__main__":
    # getters and setters
    p1 = Produto('camiseta', 50)
    p1.desconto(10)
    print(p1.preco)

    p2 = Produto('caneca', 15)
    p2.desconto(10)
    print(p2.preco)

    p3 = Produto('caneca', 50)
    p3.preco = 60
    del p3.preco
    # print(p3.preco)

    # encapsulamento
    bd = BaseDeDados()
    bd.inserir_cliente(2, 'victor')
    bd.inserir_cliente(1, 'joão')
    print()
    bd.lista_clientes()
    bd.apaga_clientes(2)
    print("victor removido")
    bd.lista_clientes()
    bd.dados_publicos = {1: 'estou disponível para acesso'}
    bd._dados_protegidos={'msg': 'Estou apenas protegido'}
    # o método privado é renomeado, para acessa-lo precisamos
    print(bd._BaseDeDados__dados)
    print(bd.dados)
    print("\natualizando todos os dados com o setter")
    bd.dados = {'clientes': {0: 'sem clientes por hoje'}}
    print(bd.dados)