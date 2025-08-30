from modelos.matriz import Matriz
from estructuras.lista import Lista

# =========================
# Funciones auxiliares
# =========================

# contar elementos en una lista enlazada
def contar_elementos(lista):
    contador = 0
    actual = lista.get_cabeza()
    while actual:
        contador += 1
        actual = actual.get_siguiente()
    return contador

# buscar posición de un id en una lista enlazada
def buscar_columna(lista_ids, id_buscar):
    actual = lista_ids.get_cabeza()
    indice = 0
    while actual:
        if actual.get_dato() == id_buscar:
            return indice
        actual = actual.get_siguiente()
        indice += 1
    return -1  # no encontrado

# =========================
# Matriz de Frecuencias
# =========================
def construir_matriz_frecuencias(campo):
    num_estaciones = contar_elementos(campo.get_estaciones())
    num_sensores_suelo = contar_elementos(campo.get_sensores_suelo())
    num_sensores_cultivo = contar_elementos(campo.get_sensores_cultivo())
    num_sensores = num_sensores_suelo + num_sensores_cultivo

    matriz = Matriz(num_sensores, num_estaciones)

    estaciones_ids = Lista()
    actual_est = campo.get_estaciones().get_cabeza()
    while actual_est:
        estaciones_ids.insertar(actual_est.get_dato().get_id())
        actual_est = actual_est.get_siguiente()

    fila = 0
    # sensores de suelo
    actual_suelo = campo.get_sensores_suelo().get_cabeza()
    while actual_suelo:
        sensor = actual_suelo.get_dato()
        actual_freq = sensor.get_frecuencias().get_cabeza()
        while actual_freq:
            freq = actual_freq.get_dato()
            j = buscar_columna(estaciones_ids, freq.get_id_estacion())
            matriz.set_valor(fila, j, freq.get_valor())
            actual_freq = actual_freq.get_siguiente()
        fila += 1
        actual_suelo = actual_suelo.get_siguiente()

    # sensores de cultivo
    actual_cultivo = campo.get_sensores_cultivo().get_cabeza()
    while actual_cultivo:
        sensor = actual_cultivo.get_dato()
        actual_freq = sensor.get_frecuencias().get_cabeza()
        while actual_freq:
            freq = actual_freq.get_dato()
            j = buscar_columna(estaciones_ids, freq.get_id_estacion())
            matriz.set_valor(fila, j, freq.get_valor())
            actual_freq = actual_freq.get_siguiente()
        fila += 1
        actual_cultivo = actual_cultivo.get_siguiente()

    return matriz, estaciones_ids

def imprimir_matriz(matriz, estaciones_ids):
    print("\nMatriz de Frecuencias (Sensores × Estaciones):")

    # cabeceras
    print("       ", end="")
    actual_id = estaciones_ids.get_cabeza()
    while actual_id:
        print(f"{actual_id.get_dato():>8}", end="")
        actual_id = actual_id.get_siguiente()
    print()

    # filas
    for i in range(matriz.get_filas()):
        print(f"Sensor {i+1:2}: ", end="")
        for j in range(matriz.get_columnas()):
            print(f"{matriz.get_valor(i,j):8}", end="")
        print()

# =========================
# Matriz de Patrones
# =========================
def construir_matriz_patrones(matriz_frec):
    filas = matriz_frec.get_filas()
    columnas = matriz_frec.get_columnas()
    matriz_pat = Matriz(filas, columnas)

    for i in range(filas):
        for j in range(columnas):
            valor = matriz_frec.get_valor(i, j)
            if valor > 0:
                matriz_pat.set_valor(i, j, 1)
            else:
                matriz_pat.set_valor(i, j, 0)

    return matriz_pat

def imprimir_matriz_patrones(matriz, estaciones_ids):
    print("\nMatriz de Patrones (0/1):")

    print("       ", end="")
    actual_id = estaciones_ids.get_cabeza()
    while actual_id:
        print(f"{actual_id.get_dato():>8}", end="")
        actual_id = actual_id.get_siguiente()
    print()

    for i in range(matriz.get_filas()):
        print(f"Sensor {i+1:2}: ", end="")
        for j in range(matriz.get_columnas()):
            print(f"{matriz.get_valor(i,j):8}", end="")
        print()

# =========================
# Matriz Reducida
# =========================
def columnas_iguales(matriz, col1, col2):
    filas = matriz.get_filas()
    for i in range(filas):
        if matriz.get_valor(i, col1) != matriz.get_valor(i, col2):
            return False
    return True

def construir_matriz_reducida(matriz_pat, estaciones_ids):
    filas = matriz_pat.get_filas()
    columnas = matriz_pat.get_columnas()

    matriz_red = Matriz(filas, 0)
    estaciones_red = Lista()

    for j in range(columnas):
        repetida = False
        k = 0
        while k < matriz_red.get_columnas():
            if columnas_iguales(matriz_pat, j, k):
                repetida = True
                break
            k += 1

        if not repetida:
            nueva = Matriz(filas, matriz_red.get_columnas() + 1)
            for fi in range(filas):
                for co in range(matriz_red.get_columnas()):
                    nueva.set_valor(fi, co, matriz_red.get_valor(fi, co))
            for fi in range(filas):
                nueva.set_valor(fi, matriz_red.get_columnas(), matriz_pat.get_valor(fi, j))
            matriz_red = nueva

            actual_id = estaciones_ids.get_cabeza()
            idx = 0
            while idx < j:
                actual_id = actual_id.get_siguiente()
                idx += 1
            estaciones_red.insertar(actual_id.get_dato())

    return matriz_red, estaciones_red

def imprimir_matriz_reducida(matriz, estaciones_ids):
    print("\nMatriz Reducida ")

    print("       ", end="")
    actual_id = estaciones_ids.get_cabeza()
    while actual_id:
        print(f"{actual_id.get_dato():>8}", end="")
        actual_id = actual_id.get_siguiente()
    print()

    for i in range(matriz.get_filas()):
        print(f"Sensor {i+1:2}: ", end="")
        for j in range(matriz.get_columnas()):
            print(f"{matriz.get_valor(i,j):8}", end="")
        print()
