my_list = [7, 5, 3, 3, 2]
new_n = int(input('Введите число - '))
i = len(my_list) - 1
if new_n >= my_list[0]:
    my_list.insert(0, new_n)
else:
    while i >= 0:
        if new_n < my_list[i]:
            my_list.insert(i+1, new_n)
            break
        i -= 1
print(my_list)

