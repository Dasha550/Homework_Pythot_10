class Road:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def volume(self, weight, height):
        print(self.length*self.width*weight*height/1000)

a = Road(20, 5000)
a.volume(25, 5)