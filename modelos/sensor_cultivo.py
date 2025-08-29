from estructuras.lista import Lista

class Sensor:
    def __init__(self, id, nombre):
        self.__id = id
        self.__nombre = nombre
        self.__frecuencias = Lista()

    def get_id(self): return self.__id
    def get_nombre(self): return self.__nombre
    def get_frecuencias(self): return self.__frecuencias

    def __str__(self):
        return f"Sensor {self.__id}: {self.__nombre}"
