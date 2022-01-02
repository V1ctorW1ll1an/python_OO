from classes.Pessoa import Pessoa

if __name__=="__main__":
    p1 = Pessoa('Victor',23)
    p1.mostrar_ano_nascimento()

    p2= Pessoa.factory_por_ano_nascimento('Victor Willian', 1998)
    print(p2.idade)