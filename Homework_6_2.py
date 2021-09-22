class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_calculation(self, height):
        BASE_MASS = 25
        self.mass = (self._length * self._width * height * BASE_MASS) / 1000
        print(f'Требуемая масса асфальта равна {self.mass} т')


trassa_e95 = Road(5000, 20)
h = int(input('Введите требуемую толщину асфальта в сантиметрах '))
trassa_e95.mass_calculation(h)
