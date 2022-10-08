from time import sleep

class TrafficLight:
    def __init__(self, color):
        self._color = color
    def running(self):
        for key, value in self._color.items():
            sleep(value)
            print(key)


Traffic = TrafficLight(color={
    "Красный": 7,
    "Желтый": 2,
    "Зеленый": 4})
Traffic.running()