my_list = input('Введите слова через пробел: ')
my_list = my_list.split(' ')
i = 1
for el in my_list:
    print(i, el[:10])
    i += 1