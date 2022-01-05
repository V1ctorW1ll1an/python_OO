from classes import Product, ShoppingCart

if __name__ == "__main__":
    shoppingCart = ShoppingCart()
    p1 = Product('mouse', 50)
    p2 = Product('iphone', 5000)
    p3 = Product('cup', 15)

    shoppingCart.insert_products(p1)
    shoppingCart.insert_products(p2)
    shoppingCart.insert_products(p3)

    shoppingCart.list_products()

    print("total:", shoppingCart.total_sum())
