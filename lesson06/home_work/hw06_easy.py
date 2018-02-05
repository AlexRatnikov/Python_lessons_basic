# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
import math

class Triangle:
    def __init__(self, peak1=(-1,0), peak2=(3,-3), peak3=(3,3)):
        self.peak1 = peak1
        self.peak2 = peak2
        self.peak3 = peak3

    def distance(self, p1, p2):
        def square(x):
            return x * x
        dist = math.sqrt(square(p2[0] - p1[0]) + square(p2[1] - p1[1]))
        return dist

    def perimeter(self):
        return self.distance(self.peak1, self.peak2) + self.distance(self.peak2, self.peak3) + self.distance(self.peak3, self.peak1)

    def area(self):
        base = (self.distance(self.peak3, self.peak1) * (1 / 2))
        height = ((base) ** 2) - (self.distance(self.peak1, self.peak2) ** 2)
        h = math.fabs(height)
        a = (1/2) * ((base) * (h))
        return a

tri = Triangle()

print(tri.perimeter())
print(tri.area())

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.