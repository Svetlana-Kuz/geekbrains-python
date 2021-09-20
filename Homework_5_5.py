with open('task5.txt', 'w+') as f:
    f.write('34.2 2 7 65 8 396')
    f.seek(0)
    num = f.read()
sum = 0
num = num.split(' ')
for i in num:
    sum = sum + float(i)
print('Сумма чисел в файле равна ', sum)
