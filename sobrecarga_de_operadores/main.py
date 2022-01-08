from classes import Retangulo

if __name__ == "__main__":
    r1 = Retangulo(10, 20)
    r2 = Retangulo(10, 20)
    r3 = r1 + r2
    print(r3)

    print(r3 > r1)
    print(r2 > r3)
    print(r3 < r2)
    print(r1 == r2)
