# sensor = object
moisture_limit = 10

moisture = 0
def measuring():
    if moisture < moisture_limit:
        #watering plants
        print("dirt humidity is under 10% watering plant ", 5, " activated")