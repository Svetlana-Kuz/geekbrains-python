def int_func(word):
    right_word = True
    for el in word:
        if el.isupper():
            right_word = False
            break
    if right_word == True:
        word = word.title();
    return word
# print(int_func(input('введите слово с маленькой буквы ')))
my_str = input('Input string ').split()
i = 0
while i < len(my_str):
    my_str[i] = int_func(my_str[i])
    i += 1
print(' '.join(my_str))

