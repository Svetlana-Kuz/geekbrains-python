n = int(input('Введите число n от 1 до 9 - '))
sum_n = 123 * n #решение конкретной задачи с упрощением выражения n+nn+nnn для чисел от 1 до 9
print(f'Сумма {n}{n}{n} + {n}{n} + {n} равна {sum_n}')


n = input('Введите любое целое число - ')
nn = int(n + n)
nnn = int(n + n + n)
n = int(n)
sum_n = n + nn + nnn
print(f'Сумма {nnn} + {nn} + {n} равна {sum_n}')