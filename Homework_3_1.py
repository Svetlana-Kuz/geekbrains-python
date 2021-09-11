# def my_div(a, b):
#     return "%.2f" % (a / b)
#
#
# a = float(input('Введите делимое - '))
# b = float(input('Введите делитель - '))
# if b == 0:
#     print('Делить на 0 нельзя!')
# else:
#     print('Результат деления: ', my_div(a, b))

def my_div(a, b):
    if b == 0:
        # print('Делить на 0 нельзя!')
        result = 'делить на ноль нельзя!'
        return result
    else:
        result = "%.2f" % (a / b)
        # print('Результат деления: ', result)
        return result


a = float(input('Введите делимое - '))
b = float(input('Введите делитель - '))
print ('Результат деления - ', my_div(a, b))