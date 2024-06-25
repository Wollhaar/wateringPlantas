from Sensors import MoistureSensor

moisture_sensors = []
for i in range(3):
    moisture_sensors.append(MoistureSensor(i, 'Iduino ME110 Bodenfeuchtesensor', 0))

# sensor = object
moisture_limit = 10

def measuring(ms):
    if ms.moisture < moisture_limit:
        #watering plants
        print("soil humidity is under 10% watering plant with sensor-ID ", ms.id, " activated")

for sensor in moisture_sensors:
    measuring(sensor)

