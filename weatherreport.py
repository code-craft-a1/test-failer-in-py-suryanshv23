
def sensorStub():
    return {
        'temperatureInC': 50,
        'precipitation': 70,
        'humidity': 26,
        'windSpeedKMPH': 52
    }

def report(sensorReader):
    readings = sensorReader()
    weather = "Sunny Day"

    if readings['temperatureInC'] > 25:
        if readings['precipitation'] >= 60:
            weather = "Rainy Day"
        elif readings['precipitation'] >= 20:
            weather = "Partly Cloudy"
        if readings['windSpeedKMPH'] > 50:
            weather = "Alert, Stormy with heavy rain"
    return weather



def stubRainy():
    return {
        'temperatureInC': 30,
        'precipitation': 70,
        'humidity': 80,
        'windSpeedKMPH': 30
    }

def stubStormy():
    return {
        'temperatureInC': 35,
        'precipitation': 55,
        'humidity': 70,
        'windSpeedKMPH': 60
    }

def stubSunny():
    return {
        'temperatureInC': 20,
        'precipitation': 0,
        'humidity': 30,
        'windSpeedKMPH': 10
    }

def stubPartlyCloudy():
    return {
        'temperatureInC': 30,
        'precipitation': 30,
        'humidity': 50,
        'windSpeedKMPH': 20
    }

def testRainy():
    weather = report(stubRainy)
    print(f"Rainy test: {weather}")
    assert("Rainy" in weather)

def testStormy():
    weather = report(stubStormy)
    print(f"Stormy test: {weather}")
    assert("Stormy" in weather)

def testSunny():
    weather = report(stubSunny)
    print(f"Sunny test: {weather}")
    assert(weather == "Sunny Day")

def testPartlyCloudy():
    weather = report(stubPartlyCloudy)
    print(f"Partly Cloudy test: {weather}")
    assert("Partly Cloudy" in weather)

if __name__ == '__main__':
    testRainy()
    testStormy()
    testSunny()
    testPartlyCloudy()
    print("All is well (maybe!)")
