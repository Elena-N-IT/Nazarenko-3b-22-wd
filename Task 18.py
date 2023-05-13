class Figure:

    def __init__(self, square, perimeter):
        self.square=square
        self.perimeter=perimeter

    def info(self):
        print("площадь -", self.square, ",", "периметр -", self.perimeter)


figure1=Figure(25, 15)
figure1.info()