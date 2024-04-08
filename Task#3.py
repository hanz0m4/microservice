import math


class figure:


    def area(self):
        pass


    def perimetr(self):
        pass


    def sravnenie_per(self, other):
        if self.perimetr() > other.perimetr():
            return "больше"
        else:
            return "меньше"


    def sravnenie_area(self, other):
        if self.area() > other.area():
            return "больше"
        else:
            return "меньше"


class krug(figure):

    def __init__(self, radius):
        self.radius = radius

    def perimetr(self):
        return 2 * math.pi * self.radius
    def area(self):
        return math.pi * self.radius ** 2


class kvadrat(figure):

    def __init__(self, storona):
        self.storona = storona

    def perimetr(self):
        return self.storona * 4

    def area(self):
        return self.storona ** 2


class pryamougolnik(figure):

    def __init__(self, dlina, shirina):
        self.dlina = dlina
        self.shirina = shirina

    def perimetr(self):
        return (self.dlina + self.shirina)*2

    def area(self):
        return self.dlina * self.shirina


class treugolnik(figure):

    def __init__(self, gipotenuza, katet1, katet2):
        self.gipotenuza = gipotenuza
        self.katet1 = katet1
        self.katet2 = katet2

    def perimetr(self):
        return self.gipotenuza + self.katet1 + self.katet2

    def area(self):
        return 0.5 * (self.katet1 + self.katet2)



k1 = kvadrat(6)
print("Площадь квадрата 1:", k1.area())
print("Периметр квадрата 1:", k1.perimetr())


p1 = pryamougolnik(4, 6)
print("Площадь прямоугольника 1:", p1.area())
print("Периметр прямоугольника 1:", p1.perimetr())


t1 = treugolnik(5, 4, 3)
print("Площадь треугольника 1:", t1.area())
print("Периметр треугольника 1:", t1.perimetr())


k1 = krug(5)
print("Площадь круга 1:", k1.area())
print("Периметр круга 1:", k1.perimetr())
print (" ")


print("Сравнение периметра квардрата с прямоугольником:", k1.sravnenie_per(p1))
print("Сравнение периметра квардрата с треугольником:", k1.sravnenie_per(t1))
print("Сравнение периметра квардрата с кругом:", k1.sravnenie_per(k1))
print (" ")


print("Сравнение периметра прямоугольника с квадратом:", p1.sravnenie_per(k1))
print("Сравнение периметра прямоугольника с треугольником:", p1.sravnenie_per(t1))
print("Сравнение периметра прямоугольника с кругом:", p1.sravnenie_per(k1))
print (" ")


print("Сравнение периметра круга с прямоугольником:", k1.sravnenie_per(p1))
print("Сравнение периметра круга с треугольником:", k1.sravnenie_per(t1))
print("Сравнение периметра круга с квадратом:", k1.sravnenie_per(k1))
print (" ")


print("Сравнение периметра треугольника с прямоугольником:", t1.sravnenie_per(p1))
print("Сравнение периметра треугольника с квадрата:", t1.sravnenie_per(k1))
print("Сравнение периметра треугольника с кругом:", t1.sravnenie_per(k1))
print (" ")


print("Сравнение площади квардрата с прямоугольником:", k1.sravnenie_area(p1))
print("Сравнение площади квардрата с треугольником:", k1.sravnenie_area(t1))
print("Сравнение площади квардрата с кругом:", k1.sravnenie_area(k1))
print (" ")


print("Сравнение площади прямоугольника с квадратом:", p1.sravnenie_area(k1))
print("Сравнение площади прямоугольника с треугольником:", p1.sravnenie_area(t1))
print("Сравнение площади прямоугольника с кругом:", p1.sravnenie_area(k1))
print (" ")


print("Сравнение площади круга с прямоугольником:", k1.sravnenie_area(p1))
print("Сравнение площади круга с треугольником:", k1.sravnenie_area(t1))
print("Сравнение площади круга с квадратом:", k1.sravnenie_area(k1))
print (" ")


print("Сравнение площади треугольника с прямоугольником:", t1.sravnenie_area(p1))
print("Сравнение площади треугольника с квадратом:", t1.sravnenie_area(k1))
print("Сравнение площади треугольника с кругом:", t1.sravnenie_area(k1))