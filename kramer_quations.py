import numpy as np
from collections import defaultdict
import re

def count_definder(arr):
    #  x = numpy.delete(x, (0), axis=0)  для строк 
    #  x = numpy.delete(x, (0), axis=1)  для столбцов 
    a = arr
    A_dict = defaultdict(str)
    for row in range(len(a)):
        for column in range(len(a[row])):
            e = np.delete(a, (row), axis=0)
            b = np.delete(e, (column), axis=1)
            ans = b[0][0]*b[1][1] - b[0][1]*b[1][0]
            A_dict[f"A{row+1}{column+1}"] = ans

    definder = 0
    A_pointer = 0
    for _ in range(len(a)):
        counted = a[0][A_pointer]*A_dict[f"A1{A_pointer+1}"]
        if A_pointer % 2:
            definder -= counted
        else:
            definder += counted
        A_pointer += 1


    return definder


def get_value(str_equat):
    if len(str_equat) == 1:
        return 1
    if str_equat[0] == '-' or str_equat[0] == '+':
        if len(str_equat[:-1]) == 1:
            sign = str_equat[:-1]
            res = float(f"{sign}1")
            return res
        res = float(str_equat[:-1])
        return res
    else:
        res = float(str_equat[:-1])
        return res

def parse_equation(equations):
    list_s = []
    for equation in equations.split(','):
        variables, b = some(equation)
        list_s.append((variables, b))

    list_b = [x[1] for x in list_s]
    definder = np.array([list_s[x][0] for x in range(len(list_s))])

    definder_dict = defaultdict(str)
    

    for idx in range(len(list_s)):
        temp = definder.copy()
        temp[:, idx] = list_b

        definder_dict[f'{idx}_def'] = temp
    definder_dict['definder'] = definder
    return definder_dict

def some(ss):
    res = re.findall(r'.?\d*?[a-zA-Z]', ss)
    b = re.search(r'= .?\d+', ss).group(0)[2:]
    out = ['1'+x if len(x) == 1 else x[0]+'1'+x[1:] if x[-2] == '-' or x[-2] == '+' else x for x in res]
    int_out = [int(x[:-1]) for x in out]
    return int_out, b

equations = input('Введите уравнение: ')
def view_equations(equations):
    sfd = "Расчет уравнения\n"
    for q in equations.split(','):
        sfd += f"\t{q}\n"
    sfd += 'по теореме Крамера'
    print(sfd)
    input('Нажмите любую клавишу для продолжения')

view_equations(equations) 
r_dict = parse_equation(equations)
answers = defaultdict(str)

for name, definder in r_dict.items():
    res = count_definder(definder)
    sfd = f"{name} => \n{definder} => {res}\n"
    answers[name] = res
    print(sfd)

for lett in list(r_dict.keys())[:-1]:
    sfd = f"{lett} = {lett}/definder = {answers[lett]}/{answers['definder']} = {answers[lett]/answers['definder']}"
    print(sfd)

input()

# print(count_definder(
#         np.array([[3, -2, 1],
#                 [-2, 1,3],
#                 [2,0,-2]]))
#                 )