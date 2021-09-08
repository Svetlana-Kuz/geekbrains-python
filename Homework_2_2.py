my_list = input('Введите список через запятую с пробелом: ')
my_list = my_list.split(', ')
i = 0
j = 1
while j < len(my_list):
    # a = my_list[i]
    # my_list[i] = my_list[j]
    # my_list[j] = a
    my_list[i], my_list[j] = my_list[j], my_list[i]
    i += 2
    j += 2
print(my_list)