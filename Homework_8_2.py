class ZeroError(Exception):
    def __init__(self, txt):
        self.txt = txt

try:
    a = float(input('Введите делимое: '))
    b = float(input('Введите делитель: '))
    if b == 0:
        raise ZeroError('Делитель не может быть равен нулю!')
    c = a / b
except ValueError:
    print('Вы ввели не число')
except ZeroError as err:
    print(err)
else:
    print(f'Все хорошо. Результат деления: {c}')
