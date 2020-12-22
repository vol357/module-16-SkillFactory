import math

class Restangle:
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def get_area(self):
        return self.width * self.height
    def print_fig(self):
        return 'прямоугольник('+str(self.x)+','+str(self.y)+','+ str(self.width)+','+str(self.height)+')'

class Square:
    def __init__(self,x,y,lenth):
        self.x = x
        self.y = y
        self.lenth = lenth
    def get_area_square(self):
        return self.lenth ** 2
    def print_fig(self):
        return 'квадрат('+str(self.x)+','+str(self.y)+','+ str(self.lenth)+')'
class Circle:
    def __init__(self,x,y,r):
        self.x = x
        self.y = y
        self.r = r
    def get_area_circle(self):
        pi = 3.14
        return math.pi * self.r ** 2
    def print_fig(self):
        return 'круг('+str(self.x)+','+str(self.y)+','+ str(self.r)+')'