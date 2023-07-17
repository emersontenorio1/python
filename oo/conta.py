class Conta(object):
    code_bank = "001"

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto {}....".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_da_conta = self.__saldo + self.__limite
        return valor_a_sacar <= valor_da_conta

    def saca(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print("O valor {} a ser sacado passou do limite disponível".format(valor))

    def transfere(self, valor,  destino):
        self.saca(valor)
        destino.deposita(valor)

    def get_saldo(self):
        return self.__saldo()

    def get_titular(self):
        return self.__titular()

    @property
    def limite(self):
        return self.__limite()

    @limite.setter
    def limite(self, new_limit):
        self.__limite = new_limit

    @staticmethod
    def cod_bank():
        return "abc"


