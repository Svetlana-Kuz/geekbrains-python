def my_sum(sum):
    num = input('Введите числа через пробел (для выхода введите q) ').split()
    i = 0
    for el in num:
        if el == 'q' or el == 'Q':
            print('Сумма введенных чисел равна ', sum)
            return
        else:
            num[i] = float(num[i])
            sum = sum + num[i]
            i +=1
    print('Сумма введенных чисел равна ', sum)
    my_sum(sum)
my_sum(0)