from classes import Client, ClientVip

if __name__ == '__main__':
    c1 = Client('victor', 23)
    c1.buy()

    print()

    c2 = ClientVip('Rose', 25, 'silva')
    c2.buy()  # from
    c2.speak()  # from People
