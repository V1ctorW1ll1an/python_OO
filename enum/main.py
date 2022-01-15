from enum import Enum, auto


class Directions(Enum):
    right = auto()
    left = auto()
    top = auto()
    bottom = auto()


def move(direction: Directions) -> str:
    if not isinstance(direction, Directions):
        raise ValueError("Cannot move in this direction!")
    return f'Moving {direction.name}'


if __name__ == "__main__":
    print(move(Directions.right))
    print(move(Directions.bottom))
    print(move(Directions.top))
    print(move(Directions.left))
