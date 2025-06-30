# Створіть абстрактний клас "Фігура" з абстрактними методами для отримання площі та периметру.
# Наслідуйте від нього декілька (> 2) інших фігур, та реалізуйте математично вірні для них методи для площі та периметру.
# Властивості по типу “довжина сторони” й т.д. повинні бути приватними, та ініціалізуватись через конструктор.
# Створіть Декілька різних об’єктів фігур, та у циклі порахуйте та виведіть в консоль площу та периметр кожної.
from abc import ABC, abstractmethod
from math import pi


class Figure(ABC):

    @abstractmethod
    def perimetre(self):
        pass
    @abstractmethod
    def area(self):
        pass

    def __str__(self):
        return f"Perimeter is {self.perimetre()}. Area is {self.area()}."


class Triangle(Figure):
    def __init__(self, side1, side2, side3):
        self._side1 = side1
        self._side2 = side2
        self._side3 = side3

    def perimetre(self):
        return self._side1 + self._side2 + self._side3

    def area(self):
        s = (self._side1 + self._side2 + self._side3) / 2
        return (s * (s - self._side1) * (s - self._side2) * (s - self._side3)) ** 0.5

    def __str__(self):
        return super().__str__() + " This is Triangle!"

class Rectangle(Figure):
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def perimetre(self):
        return 2 * (self._width + self._height)

    def area(self):
        return self._width * self._height

    def __str__(self):
        return super().__str__() + " This is Rectangle!"

class Circle(Figure):
    def __init__(self, radius):
        self._radius = radius


    def perimetre(self):
        return 2 * pi * self._radius

    def area(self):
        return pi * (self._radius) ** 2

    def __str__(self):
        return super().__str__() + " This is Circle!"

for i in range(1, 5):
    a = i + 2
    b = i + 3
    c = a + b - 1
    figures = [Triangle(a, b, c), Rectangle(i, i+2), Circle(i)]

    for figure in figures:
        print(figure)