from utils.lector_xml import cargar_xml
from utils.construir_matriz import (
    construir_matriz_frecuencias,
    imprimir_matriz,
    construir_matriz_patrones,
    imprimir_matriz_patrones,
    construir_matriz_reducida,
    imprimir_matriz_reducida
)
from utils.generar_salida import generar_xml_salida

def main():
    campos = cargar_xml("archivo_entrada.xml")  

    actual_campo = campos.get_cabeza()
    while actual_campo:
        campo = actual_campo.get_dato()
        print(f"\n Campo: {campo.get_id()}")

        matriz_frec, estaciones_ids = construir_matriz_frecuencias(campo)
        imprimir_matriz(matriz_frec, estaciones_ids)

        matriz_pat = construir_matriz_patrones(matriz_frec)
        imprimir_matriz_patrones(matriz_pat, estaciones_ids)

        matriz_red, estaciones_red = construir_matriz_reducida(matriz_pat, estaciones_ids)
        imprimir_matriz_reducida(matriz_red, estaciones_red)

        generar_xml_salida(campo, matriz_frec, estaciones_ids, matriz_pat, matriz_red, estaciones_red)

        actual_campo = actual_campo.get_siguiente()

if __name__ == "__main__":
    main()
