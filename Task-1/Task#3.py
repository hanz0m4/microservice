import math


class Figure:

    def area(self):
        pass


    def perimetr(self):
        pass


    def compare_per(self, other):
        if self.perimetr() > other.perimetr():
            return True
        else:
            return False


    def compare_area(self, other):
        if self.area() > other.area():
            return True
        else:
            return False

class Circle(Figure):

    def __init__(self, radius):
        self.radius = radius

    def perimetr(self):
        return 2 * math.pi * self.radius
    def area(self):
        return math.pi * self.radius ** 2


class Square(Figure):

    def __init__(self, side):
        self.side = side

    def perimetr(self):
        return self.side * 4

    def area(self):
        return self.side ** 2


class Rectangle(Figure):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimetr(self):
        return (self.length + self.width)*2

    def area(self):
        return self.length * self.width


class Triangle(Figure):

    def __init__(self, hypotenuse, kathete1, kathete2):
        self.hypotenuse = hypotenuse
        self.kathete1 = kathete1
        self.kathete2 = kathete2

    def perimetr(self):
        return self.hypotenuse + self.kathete1 + self.kathete2

    def area(self):
        return 0.5 * (self.kathete1 + self.kathete2)



k1 = Square(6)
print("Площадь квадрата 1:", k1.area())
print("Периметр квадрата 1:", k1.perimetr())


p1 = Rectangle(4, 6)
print("Площадь прямоугольника 1:", p1.area())
print("Периметр прямоугольника 1:", p1.perimetr())


t1 = Triangle(5, 4, 3)
print("Площадь треугольника 1:", t1.area())
print("Периметр треугольника 1:", t1.perimetr())


k1 = Circle(5)
print("Площадь круга 1:", k1.area())
print("Периметр круга 1:", k1.perimetr())
print (" ")


print("Сравнение периметра квардрата с прямоугольником:", k1.compare_per(p1))
print("Сравнение периметра квардрата с треугольником:", k1.compare_per(t1))
print("Сравнение периметра квардрата с кругом:", k1.compare_per(k1))
print (" ")


print("Сравнение периметра прямоугольника с квадратом:", p1.compare_per(k1))
print("Сравнение периметра прямоугольника с треугольником:", p1.compare_per(t1))
print("Сравнение периметра прямоугольника с кругом:", p1.compare_per(k1))
print (" ")


print("Сравнение периметра круга с прямоугольником:", k1.compare_per(p1))
print("Сравнение периметра круга с треугольником:", k1.compare_per(t1))
print("Сравнение периметра круга с квадратом:", k1.compare_per(k1))
print (" ")


print("Сравнение периметра треугольника с прямоугольником:", t1.compare_per(p1))
print("Сравнение периметра треугольника с квадрата:", t1.compare_per(k1))
print("Сравнение периметра треугольника с кругом:", t1.compare_per(k1))
print (" ")


print("Сравнение площади квардрата с прямоугольником:", k1.compare_area(p1))
print("Сравнение площади квардрата с треугольником:", k1.compare_area(t1))
print("Сравнение площади квардрата с кругом:", k1.compare_area(k1))
print (" ")


print("Сравнение площади прямоугольника с квадратом:", p1.compare_area(k1))
print("Сравнение площади прямоугольника с треугольником:", p1.compare_area(t1))
print("Сравнение площади прямоугольника с кругом:", p1.compare_area(k1))
print (" ")


print("Сравнение площади круга с прямоугольником:", k1.compare_area(p1))
print("Сравнение площади круга с треугольником:", k1.compare_area(t1))
print("Сравнение площади круга с квадратом:", k1.compare_area(k1))
print (" ")


print("Сравнение площади треугольника с прямоугольником:", t1.compare_area(p1))
print("Сравнение площади треугольника с квадратом:", t1.compare_area(k1))
print("Сравнение площади треугольника с кругом:", t1.compare_area(k1))
