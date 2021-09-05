big_number = int(input('Введите многозначное целое число - '))
biggest_n = big_number % 10
big_number = big_number // 10
while big_number > 0:
    n = big_number % 10
    if n > biggest_n:
        biggest_n = n
    big_number = big_number // 10
print('Наибольшая цифра во введенном числе - ', biggest_n)