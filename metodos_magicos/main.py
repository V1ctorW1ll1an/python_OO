from classes import A

if __name__ == "__main__":
    a = A()
    b = A()
    c = A()

    print(a == b == c)
    print(id(a), id(b), id(c))
    resultado = a(1, 2, 3, 4, 5)
    print(resultado)
