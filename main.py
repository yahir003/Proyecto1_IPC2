from utils.lector_xml import cargar_xml
from utils.construir_matriz import *
from utils.generar_salida import generar_xml_salida
from utils.generar_grafica_salida import graficar_salida

def main():
    campos = None

    while True:
        print("\n===== MENÚ PRINCIPAL =====")
        print("1. Cargar archivo XML de entrada")
        print("2. Procesar información y generar matrices")
        print("3. Generar archivo de salida XML")
        print("4. Generar gráfica (matriz reducida)")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            campos = cargar_xml("archivo_entrada.xml")
            print("✅ Archivo cargado correctamente.")

        elif opcion == "2":
            if not campos:
                print("⚠ Primero cargue un archivo XML.")
                continue

            actual_campo = campos.get_cabeza()
            while actual_campo:
                campo = actual_campo.get_dato()
                print(f"\n🌱 Campo: {campo.get_id()}")

                matriz_frec, estaciones_ids = construir_matriz_frecuencias(campo)
                imprimir_matriz(matriz_frec, estaciones_ids)

                matriz_pat = construir_matriz_patrones(matriz_frec)
                imprimir_matriz_patrones(matriz_pat, estaciones_ids)

                matriz_red, estaciones_red = construir_matriz_reducida(matriz_pat, estaciones_ids)
                imprimir_matriz_reducida(matriz_red, estaciones_red)

                generar_xml_salida(campo, matriz_frec, estaciones_ids, matriz_pat, matriz_red, estaciones_red)

                actual_campo = actual_campo.get_siguiente()

        elif opcion == "3":
            print("✅ Archivo salida.xml ya fue generado en la opción 2.")

        elif opcion == "4":
            graficar_salida()

        elif opcion == "5":
            print("👋 Saliendo del programa...")
            break

        else:
            print("⚠ Opción inválida, intente de nuevo.")
