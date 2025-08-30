import os

def exportar_matriz_dot(nombre, matriz, estaciones_ids, archivo="graficas"):
    if not os.path.exists(archivo):
        os.makedirs(archivo)

    dot_file = os.path.join(archivo, f"{nombre}.dot")
    png_file = os.path.join(archivo, f"{nombre}.png")

    with open(dot_file, "w", encoding="utf-8") as f:
        f.write("digraph G {\n")
        f.write("  node [shape=plaintext fontname=Courier];\n")
        f.write(f"  {nombre} [label=<\n")
        f.write("  <table border='1' cellborder='1' cellspacing='0'>\n")

        # cabeceras
        f.write("    <tr><td></td>")
        actual_id = estaciones_ids.get_cabeza()
        while actual_id:
            f.write(f"<td>{actual_id.get_dato()}</td>")
            actual_id = actual_id.get_siguiente()
        f.write("</tr>\n")

        # filas
        for i in range(matriz.get_filas()):
            f.write(f"    <tr><td>Sensor {i+1}</td>")
            for j in range(matriz.get_columnas()):
                f.write(f"<td>{matriz.get_valor(i,j)}</td>")
            f.write("</tr>\n")

        f.write("  </table>\n")
        f.write("  >];\n")
        f.write("}\n")

    # generar PNG (requiere tener Graphviz instalado en el sistema)
    os.system(f"dot -Tpng {dot_file} -o {png_file}")
    print(f"✅ Gráfica generada: {png_file}")
