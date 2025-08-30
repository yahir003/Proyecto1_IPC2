from estructuras.lista import Lista

class Matriz:
    def __init__(self, filas, columnas):
        self.__filas = filas
        self.__columnas = columnas
        self.__datos = Lista()  

        
        for _ in range(filas):
            fila = Lista()
            for _ in range(columnas):
                fila.insertar(0)
            self.__datos.insertar(fila)

    def set_valor(self, fila, columna, valor):
        actual_fila = self.__datos.get_cabeza()
        for i in range(fila):
            actual_fila = actual_fila.get_siguiente()
        lista_fila = actual_fila.get_dato()

        actual_col = lista_fila.get_cabeza()
        for j in range(columna):
            actual_col = actual_col.get_siguiente()
        actual_col.set_dato(valor)

    def get_valor(self, fila, columna):
        actual_fila = self.__datos.get_cabeza()
        for i in range(fila):
            actual_fila = actual_fila.get_siguiente()
        lista_fila = actual_fila.get_dato()

        actual_col = lista_fila.get_cabeza()
        for j in range(columna):
            actual_col = actual_col.get_siguiente()
        return actual_col.get_dato()

    def imprimir(self):
        actual_fila = self.__datos.get_cabeza()
        while actual_fila:
            lista_fila = actual_fila.get_dato()
            actual_col = lista_fila.get_cabeza()
            fila_str = ""
            while actual_col:
                fila_str += f"{actual_col.get_dato():5}"
                actual_col = actual_col.get_siguiente()
            print(fila_str)
            actual_fila = actual_fila.get_siguiente()

    def get_filas(self): return self.__filas
    def get_columnas(self): return self.__columnas
