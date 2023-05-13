class Recttangle:
    def __init__(self, height, width):
        self.height=height
        self.width=width
    def square(self):
        print("Площадь прямоугольника равна", self.width * self.height)

recttangle1=Recttangle(12, 31)

recttangle1.square()