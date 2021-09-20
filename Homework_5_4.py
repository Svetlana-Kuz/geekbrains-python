num_translate = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}
with open('task4.txt') as f:
    for line in f:
        num = line.split(' - ')
        num[0] = num_translate.get(num[0])
        num_str = ' - '.join(num)
        with open('task4_new.txt', 'a') as new_f:
            new_f.write(num_str)