from restangle import Restangle, Square, Circle

rest_1 = Restangle(0,0,3,4)
rest_2 = Restangle(0,0,12,5)
square_1 = Square(0,0,5)
square_2 = Square(0,0,10)
circle_1 = Circle(0,0,5)
circle_2 = Circle(0,0,10)

figures = [rest_1, rest_2, square_1, square_2, circle_1, circle_2]

for figure in figures:
    print('фигура - '+figure.print_fig())
    if isinstance(figure, Square):
        a=(figure.get_area_square())
    elif isinstance(figure, Restangle):
        a=(figure.get_area())
    elif isinstance(figure, Circle):
        a=(figure.get_area_circle())
    print('площадь равна: '+str(round(a,2)))