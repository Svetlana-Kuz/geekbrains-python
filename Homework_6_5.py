class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print('Аккуратно, ручка не стрирается!')

class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print('Лучше возьми маркер!')

class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print('Выходит красочная картинка!')

my_pen = Pen('Parker')
my_pencil = Pencil('простой карандаш')
my_handle = Handle('оранжевый маркер')
my_pen.draw()
my_pencil.draw()
my_handle.draw()