# через возведение в степень

# def neg_exp(x, y):
#     return x ** y
# x = float(input('Введите действительное положительное число '))
# y = int(input('Введите целое отрицательное число '))
# print(f'{x} в степени {y} равно ', neg_exp(x, y))

# через цикл

def neg_exp(x, y):
    i = 0
    exp = 1
    while i > y:
        exp = exp * (1 / x)
        i -= 1
    return exp


x = float(input('Введите действительное положительное число '))
y = int(input('Введите целое отрицательное число '))
print(f'{x} в степени {y} равно ', neg_exp(x, y))
