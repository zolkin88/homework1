class Figure:
    @property
    def name(self):
        pass

    @property
    def area(self):
        pass

    @property
    def angles(self):
        pass

    @property
    def perimeter(self):
        pass

    def add_square(self, figure):
        return self.area + figure.area
