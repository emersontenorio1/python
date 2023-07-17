class Cliente:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        print("Chamando o Property nome")
        return self.__nome.title()

    @nome.setter
    def nome(self, nome):
        print("chamando o setters nome()")
        self.__nome = nome
