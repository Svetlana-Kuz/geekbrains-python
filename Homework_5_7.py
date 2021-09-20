import json
firm_result = {}
sum_result = 0
i = 0
with open('task7.txt') as f:
    for line in f:
        about_firm = line.split()
        firm_result[about_firm[0]] = int(about_firm[2]) - int(about_firm[3])
        if firm_result[about_firm[0]] > 0:
            sum_result = sum_result + firm_result[about_firm[0]]
            i += 1
average = {'average profit': sum_result / i}
firm_result_with_av = [firm_result, average]
print(firm_result_with_av)
with open('task7.json', 'w') as new_f:
    json.dump(firm_result_with_av, new_f)