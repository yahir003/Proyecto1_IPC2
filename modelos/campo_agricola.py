from estructuras.lista import Lista

class CampoAgricola:
    def __init__(self, id, nombre):
        self.__id = id
        self.__nombre = nombre
        self.__estaciones = Lista()
        self.__sensores_suelo = Lista()
        self.__sensores_cultivo = Lista()

    def get_id(self): return self.__id
    def get_nombre(self): return self.__nombre
    def get_estaciones(self): return self.__estaciones
    def get_sensores_suelo(self): return self.__sensores_suelo
    def get_sensores_cultivo(self): return self.__sensores_cultivo

    def __str__(self):
        return f"CampoAgricola {self.__id}: {self.__nombre}"
