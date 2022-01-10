# from classes import Arquivo
from classes import abrir

if __name__ == "__main__":
    # with Arquivo('abc.txt', 'w') as f:
    #     f.write('Alguma coisa')
    with abrir('abc.txt', 'w') as file:
        file.write("ola mundo")
