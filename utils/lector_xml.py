import xml.etree.ElementTree as ET
from estructuras.lista import Lista
from modelos.campo_agricola import CampoAgricola
from modelos.estacion import Estacion
from modelos.sensor_suelo import SensorSuelo
from modelos.sensor_cultivo import SensorCultivo
from modelos.frecuencia import Frecuencia

def cargar_xml(ruta):
    tree = ET.parse(ruta)
    root = tree.getroot()
    lista_campos = Lista()   

    for campo in root.findall("campo"):
        c = CampoAgricola(campo.get("id"), campo.get("nombre"))

   
        for est in campo.find("estacionesBase").findall("estacion"):
            c.get_estaciones().insertar(Estacion(est.get("id"), est.get("nombre")))

       
        for sensor_s in campo.find("sensoresSuelo").findall("sensorS"):
            s = SensorSuelo(sensor_s.get("id"), sensor_s.get("nombre"))
            for freq in sensor_s.findall("frecuencia"):
                s.get_frecuencias().insertar(Frecuencia(freq.get("idEstacion"), int(freq.text)))
            c.get_sensores_suelo().insertar(s)

      
        for sensor_t in campo.find("sensoresCultivo").findall("sensorT"):
            s = SensorCultivo(sensor_t.get("id"), sensor_t.get("nombre"))
            for freq in sensor_t.findall("frecuencia"):
                s.get_frecuencias().insertar(Frecuencia(freq.get("idEstacion"), int(freq.text)))
            c.get_sensores_cultivo().insertar(s)

        lista_campos.insertar(c)

    return lista_campos
