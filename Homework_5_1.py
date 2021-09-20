my_file = open('new_file.txt', 'a')
while True:
    str = input('Введите строку ')
    if '' \
       '' == str:
        break
    else:
        my_file.write(str)
        my_file.write('\n')
        my_file.flush()
my_file.close()
