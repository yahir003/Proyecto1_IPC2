import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom

def guardar_pretty_xml(raiz, archivo):
  
    xml_str = ET.tostring(raiz, encoding="utf-8")
    parsed = minidom.parseString(xml_str)
    pretty_xml = parsed.toprettyxml(indent="  ")

    with open(archivo, "w", encoding="utf-8") as f:
        f.write(pretty_xml)

def generar_xml_salida(campo, matriz_frec, estaciones_ids, matriz_pat, matriz_red, estaciones_red, archivo="salida.xml"):
  

    raiz = ET.Element("salida")
    campo_xml = ET.SubElement(raiz, "campo", {"id": campo.get_id()})

    matriz_xml = ET.SubElement(campo_xml, "matriz", {"nombre": "frecuencias"})
    actual_est = estaciones_ids.get_cabeza()
    col_index = 0
    while actual_est:
        est_id = actual_est.get_dato()
        col_xml = ET.SubElement(matriz_xml, "columna", {"estacion": est_id})

        for fila in range(matriz_frec.get_filas()):
            val = matriz_frec.get_valor(fila, col_index)
            ET.SubElement(col_xml, "valor").text = str(val)
        actual_est = actual_est.get_siguiente()
        col_index += 1

    matriz_xml = ET.SubElement(campo_xml, "matriz", {"nombre": "patrones"})
    actual_est = estaciones_ids.get_cabeza()
    col_index = 0
    while actual_est:
        est_id = actual_est.get_dato()
        col_xml = ET.SubElement(matriz_xml, "columna", {"estacion": est_id})

        for fila in range(matriz_pat.get_filas()):
            val = matriz_pat.get_valor(fila, col_index)
            ET.SubElement(col_xml, "valor").text = str(val)
        actual_est = actual_est.get_siguiente()
        col_index += 1

    matriz_xml = ET.SubElement(campo_xml, "matriz", {"nombre": "reducida"})
    actual_est = estaciones_red.get_cabeza()
    col_index = 0
    while actual_est:
        est_id = actual_est.get_dato()
        col_xml = ET.SubElement(matriz_xml, "columna", {"estacion": est_id})

        for fila in range(matriz_red.get_filas()):
            val = matriz_red.get_valor(fila, col_index)
            ET.SubElement(col_xml, "valor").text = str(val)
        actual_est = actual_est.get_siguiente()
        col_index += 1

    guardar_pretty_xml(raiz, archivo)
    print(f"\Archivo{archivo} generado correctamente.")
   