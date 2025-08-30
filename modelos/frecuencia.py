class Frecuencia:
    def __init__(self, id_estacion, valor):
        self.__id_estacion = id_estacion
        self.__valor = valor

    def get_id_estacion(self): return self.__id_estacion
    def get_valor(self): return self.__valor

    def __str__(self):
        return f"{self.__id_estacion} -> {self.__valor}"
