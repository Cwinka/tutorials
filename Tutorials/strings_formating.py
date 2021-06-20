person = dict(name="Jehn", age=23)
sentence = 'My name is {} and I am {} years old.'.format(person["name"], person["age"])
print(sentence, "\n\n")


sentence2 = 'My name is {0} and I am {1} years old.'.format(person["name"], person["age"])
print(sentence2, "\n\n")


tag = 'hl'
text = 'This is a headline'
sentence3 = "<{0}>{1}</{0}>". format(tag, text)
print(sentence3, "\n\n")


sentence4 = 'My name is {0[name]} and I am {0[age]} years old.'.format(person) #likewise with a list by using indexing
print(sentence4, "\n\n")


class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
pl = Person("Jack", 33)
sentence5 = 'My name is {0.name} and I am {0.age} years old.'.format(pl) #likewise with a list by using indexing
print(sentence5, "\n\n")


sentence6 ='My name is {name} and I am {age} years old.'.format(name="Jegn", age=23) #likewise with a list by using indexing
print(sentence6, "\n\n")

sentence7 = 'My name is {name} and I am {age} years old.'.format(**person) #likewise with a list by using indexing
print(sentence7, "\n\n")

for i in range(1, 11):
    sentence = "The valuse is {:02}".format(i)
    print(sentence)


pi = 3.14159265
sentence8 = "Pi is equal to {:.4f}".format(pi)
print('\n', sentence8, "\n\n")


sentence9 = "1 MB is equal to {:,.2f} bytes".format(1000**2)
print(sentence9, "\n\n")


import datetime
my_date = datetime.datetime(2019, 10, 6, 17, 00, 50)
print(my_date, "\n\n")


sentence10 = '{:%B %d, %Y }'.format(my_date)
print(sentence10, "\n\n")

sentence11 = "{0:%B %d, %Y}, fell on a {0:%A} and was the {0:%j} day of the year".format(my_date)
print(sentence11)
