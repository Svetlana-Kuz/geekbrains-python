subjects = {}
with open('task6.txt', 'r', encoding='utf-8') as f:
    for line in f:
        subj = line.replace('(', ' ').split()
        sum = 0
        for i in subj:
            if i.isdigit() == True:
                sum = sum + int(i)
        subjects[subj[0]] = sum
print(subjects)