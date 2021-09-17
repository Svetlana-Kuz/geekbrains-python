data = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_data = [i for i in data if i > data[data.index(i)-1] and data.index(i) > 0]
print(new_data)