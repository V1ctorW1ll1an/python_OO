class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.addresses = []

    def insert_address(self, city, state):
        address = Address(city, state)
        self.addresses.append(address)

    def list_address(self):
        for address in self.addresses:
            print(address.city, address.state)

    def __del__(self):
        print(f'{self.name} has been deleted!')


class Address:
    def __init__(self, city, state):
        self.city = city
        self.state = state

    def __del__(self):
        print(f'{self.city}/{self.state} has been deleted!')
