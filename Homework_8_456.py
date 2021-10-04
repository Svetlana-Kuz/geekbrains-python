class Storage:
    def __init__(self):
        self._dict = {}

    def add_to(self, equipment, amount):
        if amount.isdigit():
            self._dict.setdefault(equipment.key_name, [int(amount)])
        else:
            print('Неверный тип данных, оборудование не добавлено на склад')

    def extract(self, name):
        self._dict.pop(name)



class Equipment:
    def __init__(self, name, series, year: int):
        self.name = name
        self.series = series
        self.year = year
        self.key = self.name + ' ' + str(self.series) + ' ' + str(self. year)

    @property
    def key_name(self):
        return f'{self.key}'

    def about(self):
        return f'{self.name} {self.series} {self.year}'

class Printer(Equipment):
    def __init__(self, name, series, year: int, is_colour: bool, printer_type = 'laser' or 'jet'):
        super().__init__(name, series, year)
        self.is_colour = is_colour
        self.printer_type = printer_type


class Scaner(Equipment):
    def __init__(self, name, series, year: int, speed: int):
        super().__init__(name, series, year)
        self.speed = speed


class MFD(Equipment):
    def __init__(self, name, series, year: int, is_colour: bool):
        super().__init__(name, series, year)
        self.is_colour = is_colour



storage = Storage()
printer1 = Printer('Epson', 'L805', 2021, True, 'laser')
storage.add_to(printer1, input(f'Введите количество {printer1.key_name} '))
scaner1 = Scaner('Canon', 'CanoScan LiDE400', 2020, 4)
storage.add_to(scaner1, input(f'Введите количество {scaner1.key_name} '))
scaner2 = Scaner('Plustek', 'OpticBook', 2021, 7)
storage.add_to(scaner2, input(f'Введите количество {scaner2.key_name} '))
xerox = MFD('Xerox', 'WorkCentre 3025', 2020, True)
storage.add_to(xerox, input(f'Введите количество {xerox.key_name} '))
print(storage._dict)
storage.extract(printer1.key_name) #удаляет полностью со склада, по идее надо часть удалять, но я что-то не успеваю реализовать
print(storage._dict)