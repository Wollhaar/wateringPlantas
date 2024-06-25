from Sensor import Sensor

class MoistureSensor(Sensor):
    def __init__(self, id, name, value):
        super().__init__('M-' + str(id), name, 'moisture', value)
        self.moisture = value / 100


MoistureSensor(12, 'Bodensensor', 11)
