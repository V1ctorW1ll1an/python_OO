from composicao.classes import People

if __name__ == "__main__":
    people = People('Victor', 23)
    people.insert_address('Belo Horizonte', 'MG')
    people.list_address()
    del people

    people2 = People('Maria', 65)
    people2.insert_address("Coronel Fabriciano", "MG")
    people2.insert_address("Rio de Janeiro", "RJ")

    people2.list_address()

    print("################################")
