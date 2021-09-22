class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Автомобиль {self.name}, цвет - {self.color}, начал движение')

    def stop(self):
        print(f'Автомобиль {self.name}, цвет - {self.color}, прекратил движение')

    def turn(self, direction):
        print(f'Автомобиль {self.name}, цвет - {self.color}, повернул {direction}')

    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.name}, цвет - {self.color}, составляет {self.speed} км/ч')

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        if self.speed > 60:
            print(f'Автомобиль {self.name}, цвет - {self.color}, скорость {self.speed}. Превышение допустимой скорости!')
        else:
            print(f'Текущая скорость автомобиля {self.name}, цвет - {self.color}, составляет {self.speed} км/ч')

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print(f'Автомобиль {self.name}, цвет - {self.color}, скорость {self.speed}. Превышение допустимой скорости!')
        else:
            print(f'Текущая скорость автомобиля {self.name}, цвет - {self.color}, составляет {self.speed} км/ч')

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


first_car = TownCar(70, 'синий', 'mazda', False)
print(first_car.name, first_car.is_police)
second_car = SportCar(130, 'красный', 'ferrari', False)
third_car = WorkCar(30, 'черный', 'волга', False)
fourth_car = PoliceCar(60, 'белый', 'renault', True)
first_car.go()
second_car.go()
first_car.show_speed()
third_car.go()
third_car.show_speed()
third_car.speed = 100
third_car.show_speed()
second_car.turn('налево')
third_car.stop()