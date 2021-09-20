# import json
#
# with open('workers.json', 'r') as f:
#     workers_salary = json.load(f)
#
# min_salary = []
# sum_salary = 0
# i = 0
# for name, salary in workers_salary.items():
#     sum_salary = sum_salary + salary
#     i +=1
#     if salary < 20000:
#         min_salary.append(name)
# print('Список работников с зарплатой меньше 20000: \n', min_salary)
# mid_salary = sum_salary / i
# print('Средняя зарплата составляет: ', '%.2f' % mid_salary)


min_salary = []
sum_salary = 0
i = 0
with open('workers.txt', 'r', encoding='utf-8') as f:
    for line in f:
        worker_salary = line.split()
        sum_salary = sum_salary + float(worker_salary[1])
        i +=1
        if float(worker_salary[1]) < 20000: min_salary.append(worker_salary[0])

print('Список работников с зарплатой меньше 20000: \n', min_salary)
mid_salary = sum_salary / i
print('Средняя зарплата составляет: ', '%.2f' % mid_salary)
