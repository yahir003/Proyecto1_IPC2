class Nodo:
    def __init__(self, dato):
        self.__dato = dato
        self.__siguiente = None

    def get_dato(self):
        return self.__dato

    def set_dato(self, nuevo_dato):
        self.__dato = nuevo_dato

    def get_siguiente(self):
        return self.__siguiente

    def set_siguiente(self, nodo):
        self.__siguiente = nodo
