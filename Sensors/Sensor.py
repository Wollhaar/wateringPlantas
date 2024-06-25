class Sensor:
    def __init__(self, id, name, type, value):
        self.id = id
        self.name = name
        self.type = type
        self.value = value

    def measure(self, value):
        self.value = value


class TemperatureSensor(Sensor):
    def __init__(self, id, name, type, value):
        super().__init__(id, name, type, value)
        self.unit = 'Grad'


s1 = Sensor(1, 'name', 'none', 11)
s2 = TemperatureSensor(2, 'temp', 'temp', 30)

