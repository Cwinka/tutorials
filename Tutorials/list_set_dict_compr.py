
create_lsit = [x for x in range(10)]
print(create_lsit, "\n ---------------")


create_nested_list = [(x, y) for x in range(3) for y in range(3)]
print(create_nested_list)

name = ["Here", "lies", "names", "of", "heros"]
words = ["just", "usual", "words", "here", "there"]
create_dict = {name: value for name, value in zip(name, words)}
print (create_dict, "\n ---------------")


rand = [1,3,4,5,1,35,21,51,2,2,51,1,5,1]
create_set = {x for x in rand}
print(create_set, "\n ---------------")


create_generator = (x for x in range(10))
for i in create_generator:
    print(i)
