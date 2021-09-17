from itertools import count, cycle

# start = int(input('Введите начальное значение '))
# stop = int(input('Введите конечное значение '))
# for el in count(start):
#     if el > stop:
#         break
#     else:
#         print(el)
data = [1, 2, 10, 'You are the best!', True]
i = 0
j = int(input('Введите необходимое количество повторений '))
for el in cycle(data):
    if i > j * len(data):
        break
    else:
       print(el)
       i += 1

