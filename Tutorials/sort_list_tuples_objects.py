li = [1,2,5,9,4,6,8,7,3]
s_li = sorted(li) # return a new list and that we must have new variable
print("Sorted variable: ", s_li, "\n ----------")


#li.sort() #  sort list without creating new copy of the list
# print(li)


s_li2 = sorted(li, reverse=True)
print("Sorted reversed variable: ", s_li2, "\n ---------------")


tup = (9,1,8,2,6,4,5,3)
s_tup = sorted(tup) #return sorted list of tuples
print(s_tup, " Sorted tuple\n --------------")


di = {'name':'Corey', 'kob':"programming", 'age':None, 'os':'Windows'}
s_di = sorted(di) #IMPORTANT : return a list of keys
print(s_di, "Sorted dict \n --------------")


li3 = [-6,-5,-2,1,2,3]
s_li3 = sorted(li3, key=abs) # abs = absolute value
# (doesn't matter negative or positive)
print(s_li3, "Sorted with key\n ------------------")


class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    def __repr__(self):
        return f"({self.name}, {self.age},${self.salary})" #return a string with these values
e1 = Employee('Carl', 37, 70000)
e2 = Employee('Sarah', 29, 80000)
e3 = Employee('John', 43, 90000)
employee = [e1,e2,e3]
print(employee, "Original lsit of the classes")
def e_sorted(emp):
    return emp.name #use a variagle of the class
#Another way to write a sort func
# s_employee = sorted(employee, key=lambda e: e.name)
s_employee = sorted(employee, key=e_sorted) # also can use a "reverse" param.
s1_employee = sorted(employee, key=e_sorted, reverse=True)
print(s_employee, "Sorted list of the classes")
print(s1_employee, "Sorted reversed list of the classes")
