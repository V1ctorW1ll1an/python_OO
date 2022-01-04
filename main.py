from classes.Produto import Produto

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
    print(p3.preco)