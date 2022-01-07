from classes import Poupanca, ContaCorrente

if __name__ == "__main__":
    cp = Poupanca(111, 222, 0)
    cp.depositar(10)
    cp.sacar(5)
    cp.sacar(5)
    cp.sacar(5)
    print("################################")
    cc = ContaCorrente(agencia=555, conta=222, saldo=0, limite=500)
    cc.depositar(valor=100)
    cc.sacar(250)
    cc.sacar(500)
