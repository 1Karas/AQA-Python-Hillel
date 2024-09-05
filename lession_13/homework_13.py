
class Rhombus:
    def __init__(self, side_a, corner_a):
        self.set_side_a(side_a)
        self.set_angle_a(corner_a)

    def set_side_a(self, side_a):
        if side_a <= 0:
            raise ValueError("Сторона ромба повинна бути більше 0")
        setattr(self, 'side_a', side_a)

    def set_angle_a(self, corner_a):
        if not (0 < corner_a < 180):
            raise ValueError("Кут А повинен бути між 0 і 180 градусами")
        setattr(self, 'corner_a', corner_a)
        setattr(self, 'corner_b', 180 - corner_a)

    def __str__(self):
        return f"Ромб: Сторона = {self.side_a}, Кут А = {self.corner_a}, Кут Б = {self.corner_b}"

romb = Rhombus(5, 60)
print(romb)


