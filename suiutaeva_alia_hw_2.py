class Figure:
    unit = 'cm'

    def __init__(self):
        self.__perimeter = 0

    @property
    def perimeter(self):
        return self.__perimeter

    @perimeter.setter
    def perimeter(self, value):
        self.__perimeter = value

    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass

    def info(self):
        pass


class Square(Figure):
    def __init__(self, side_length):
        super().__init__()
        self.__side_length = side_length
        self.perimeter = self.calculate_perimeter()

    def calculate_area(self):
        return self.__side_length ** 2

    def calculate_perimeter(self):
        return self.__side_length * 4

    def info(self):
        return (f'Square side length: {self.__side_length}{self.unit}, '
                f'perimeter: {self.perimeter}{self.unit}, '
                f'area: {self.calculate_area()}{self.unit}')


class Rectangle(Figure):
    def __init__(self, length, width):
        super().__init__()
        self.__length = length
        self.__width = width
        self.perimeter = self.calculate_perimeter()

    def calculate_area(self):
        return self.__length * self.__width

    def calculate_perimeter(self):
        return (self.__length + self.__width) * 2

    def info(self):
        return (f'Rectangle length: {self.__length}{self.unit}, width: {self.__width}{self.unit}, '
                f'perimeter: {self.perimeter}{self.unit}, '
                f'area: {self.calculate_area()}{self.unit}')


figures = [
    Square(2), Square(10),
    Rectangle(5, 6),
    Rectangle(3, 10),
    Rectangle(10, 10)
]

for figure in figures:
    print(figure.info())
