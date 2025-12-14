import math
class Rhombus:
    def __init__(self, side_a: float, angle_a: float):
        self.side_a = side_a
        self.angle_a = angle_a
    def __setattr__(self, name, value):
        if name == "side_a":
            if value <= 0:
                raise ValueError("Довжина сторони повинна бути більше 0")
            super().__setattr__(name, value)
        elif name == "angle_a":
            if not(0 < value < 180):
                raise ValueError("Кут повинен бути між 0 та 180 градусами")
            super().__setattr__(name, value)
            super().__setattr__("angle_b", 180 - value)
        elif name == "angle_b":
            raise AttributeError("angle_b обчислюється автоматично")
        else:
            super().__setattr__(name, value)
    def __repr__(self):
        return f"Rhombus(side_a={self.side_a}, angle_a={self.angle_a}, angle_b={self.angle_b})"
r = Rhombus (10, 20)
print(r)


