"""
1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""

import collections


def aver_profit(named_tuple):
    return sum(named_tuple) / len(named_tuple)


company = collections.namedtuple('company', 'name q1 q2 q3 q4 aver')

company_list = []

num_company = int(input('Введите количество компаний: '))

for _ in range(num_company):
    name = input('Введите наименование компании: ')
    quarters = [float(input(f'Введите прибыль за {i + 1} квартал: ')) for i in range(4)]
    quarters.append(aver_profit(quarters))
    company_list.append(company(name, *quarters))

all_aver = []
for company in company_list:
    all_aver.append(company.aver)

average_profit = aver_profit(all_aver)
# print(average_profit)
min = []
max = []

for company in company_list:
    if company.aver <= average_profit:
        min.append(company.name)
    else:
        max.append(company.name)

print(f'\nКомпании с прибылью выше средней:\n {", ".join(max)} \n \n ')

print(f'Компании с прибылью не выше средней:\n {", ".join(min)}')


'''
Введите количество компаний: 3
Введите наименование компании: 1
Введите прибыль за 1 квартал: 1
Введите прибыль за 2 квартал: 1
Введите прибыль за 3 квартал: 1
Введите прибыль за 4 квартал: 1
Введите наименование компании: 2
Введите прибыль за 1 квартал: 2
Введите прибыль за 2 квартал: 2
Введите прибыль за 3 квартал: 2
Введите прибыль за 4 квартал: 2
Введите наименование компании: 3
Введите прибыль за 1 квартал: 3
Введите прибыль за 2 квартал: 3
Введите прибыль за 3 квартал: 3
Введите прибыль за 4 квартал: 3
2.0

Компании с прибылью выше средней:
 3 
 
 
Компании с прибылью не выше средней:
 1, 2
'''


