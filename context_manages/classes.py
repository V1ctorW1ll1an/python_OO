"""
class Arquivo:
    def __init__(self, file, mode):
        print("abrindo arquivo")
        self.file = open(file, mode)

    def __enter__(self):
        print("retornando arquivo")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("fechando arquivo")
        self.file.close()
        print(exc_type)
        print(exc_val)
        print(exc_tb)
"""

from contextlib import contextmanager


@contextmanager
def abrir(arquivo, modo):
    try:
        print("abrindo arquivo")
        arquivo = open(arquivo, modo)
        yield arquivo
    finally:
        print("fechando arquivo")
        arquivo.close()
