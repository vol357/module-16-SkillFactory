from restangle import Restangle, Square, Circle

rest_1 = Restangle(3, 4)
rest_2 = Restangle(12, 5)
square_1 = Square(5)
square_2 = Square(10)
circle_1 = Circle(5)
circle_2 = Circle(10)

figures = [rest_1, rest_2, square_1, square_2, circle_1, circle_2]

for figure in figures:
    if isinstance(figure, Square):
        print(figure.get_area_square())
    elif isinstance(figure, Restangle):
        print(figure.get_area())
    elif isinstance(figure, Circle):
        print(figure.get_area_circle())
