i = 0
with open('test_file.txt') as f_obj:
    for line in f_obj:
        i +=1
print('Количество строк в файле = ', i)
