class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.class_name = self.__class__.__name__

    def speak(self):
        print('People talking...')


class Client(People):
    def buy(self):
        print('Client buying...')

    def speak(self):
        print('Client talking...')


class ClientVip(Client):

    # sobrepondo construtor
    def __init__(self, name, age, surname):
        super().__init__(name, age)
        self.surname = surname
        #     or
        # People.__init__(name, age)

    def speak(self):
        # se refere ao construtor da super classe
        People.speak(self)
        Client.speak(self)
        print(f'{self.name} {self.surname}')
