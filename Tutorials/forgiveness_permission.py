# class Duck():
#     def quack(self):
#         print("Quack quack")
#     def fly(self):
#         print('Flap flap')
# class Person():
#     def quack(self):
#         print("I'm quacking like a duck")
#     def fly(self):
#         print("I'm flapping my arms")
#
#Pythonic
# def quack_and_fly(thing):
#     try:
#         thing.quack()
#         thing.fly()
#         thing.ddd()
#         print()
#     except Exception as e:
#         print(e)
# d = Duck()
# quack_and_fly(d)
# p = Person()
# quack_and_fly(p)
#
#



# person = {'name': 'Jess', 'age': 23, 'job': 'Programmer'}
person = {'name': 'Jess', 'age': 23}
# Non-Pythonic
# if 'name' in person and 'age' in person and 'job' in person:
#     print("I'm {name}. I'm {age} years old and my job is {job}".format(**person))
# else:
#     print("Missing some keys")

#Pythonic
# try:
#     print("I'm {name}. I'm {age} years old and my job is {job}".format(**person))
# except KeyError as e:
#     print(f'Missing {e}')



my_list = [1,2,3,4,5,6,7]
# Non-Pythonic
# if len(my_list) >= 7:
#     print(my_list[6])
# else:
#     print('Index does not exist')

#Pythonic
# try:
#     print(my_list[6])
# except IndexError:
#     print('Index does not exist')


import os
my_file = '/Scripts/demo.txt'

#Race Condition
# if os.access(my_file, os.R_OK):
#     with open(my_file) as f:
#         print(f.read())
# else:
#     print('File can not be accessed')

#No Race-Condition
try:
    f = open(my_file)
except IOError as e:
    print("File can not be accessed")
else:
    with f:
        print(f.read())
