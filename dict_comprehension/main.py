if __name__ == '__main__':
    lista = [
        ('chave', 1),
        ('chave2', 2),
    ]

    d1 = {key: value * 2 for key, value in lista}
    print(d1)
    # l1 = dict(lista)
    # print(l1)
    d1 = {key.upper(): value * 2 for key, value in lista}
    print(d1)
