from modelos.sensor import Sensor

class SensorSuelo(Sensor):
    def __init__(self, id, nombre):
        super().__init__(id, nombre)

    def __str__(self):
        return f"SensorSuelo {self.get_id()}: {self.get_nombre()}"
