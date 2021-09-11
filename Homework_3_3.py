def my_func(a, b, c):
    # сумма через сравнение элементов
    if b >= a <= c:
        sum = b + c
    elif a >= b <= c:
        sum = a + c
    else:
        sum = a + b

# просто из полной суммы вычитаем минимальное число
#     d = min(a, b, c)
#     sum = a + b + c - d
    return sum

print('Сумма наибольших чисел равна ', my_func(float(input('введите первое число ')), float(input('введите второе число ')), float(input('введите третье число '))))

# Если все числа вводить одновременно

# num = input('Введите три числа через пробел ').split()
# i = 0;
# for el in num:
#     num[i] = float(el)
#     i +=1
#
# print(num)
# print(my_func(num[0], num[1], num[2]))