class Retangulo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Retangulo(novo_x, novo_y)

    def __repr__(self):
        return f"<class 'Retangulo({self.x}, {self.y})'>"

    def __lt__(self, other):
        a1 = self.get_area()
        a2 = other.get_area()

        if a1 < a2:
            return True
        return False

    def __gt__(self, other):
        a1 = self.get_area()
        a2 = other.get_area()

        if a1 > a2:
            return True
        return False

    def __eq__(self, other):
        return bool(self.x == other.x and self.y == other.y)

    def get_area(self):
        return self.x * self.y
