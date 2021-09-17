data = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_data = [i for i in data if data.count(i) == 1]
print(new_data)