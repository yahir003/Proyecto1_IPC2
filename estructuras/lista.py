from estructuras.nodo import Nodo

class Lista:
    def __init__(self):
        self.__cabeza = None

    def insertar(self, dato):
        nuevo = Nodo(dato)
        if not self.__cabeza:
            self.__cabeza = nuevo
        else:
            actual = self.__cabeza
            while actual.get_siguiente():
                actual = actual.get_siguiente()
            actual.set_siguiente(nuevo)

    def recorrer(self):
        actual = self.__cabeza
        while actual:
            print(actual.get_dato())
            actual = actual.get_siguiente()

    def get_cabeza(self):
        return self.__cabeza
