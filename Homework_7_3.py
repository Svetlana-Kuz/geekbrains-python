class Cell:
    cell_amount =0
    def __init__(self, amount):
        self.amount = amount #задается количество ячеек в клетке
        Cell.cell_amount +=1 # параметр, соответствующий количеству клеток (целое число)

    def __add__(self, other):
        new_cell = Cell(self.amount + other.amount)
        return new_cell

    def __sub__(self, other):
        if self.amount - other.amount > 0:
            new_cell = Cell(self.amount - other.amount)
            return new_cell
        else:
            return print('Вычитание невозможно, разность меньше или равна нулю')

    def __mul__(self, other):
        new_cell = Cell(self.amount * other.amount)
        return new_cell

    def __truediv__(self, other):
        new_cell = Cell(self.amount // other.amount)
        return new_cell

    def make_order(self, num):
        order_str = ''
        for i in range(self.amount // num):
            for j in range(num):
                order_str = order_str + '*'
            if i < self.amount // num - 1:
                order_str = order_str + '\n'
        if self.amount % num > 0:
            order_str = order_str + '\n'
            for j in range(self.amount % num):
                order_str = order_str + '*'
        return order_str

cell_1 = Cell(3)
cell_2 = Cell(8)
cell_3 = cell_1 * cell_2
print(cell_3.make_order(5))
cell_4 = cell_1 - cell_2
print((cell_2 / cell_1).amount)
print(Cell.cell_amount)