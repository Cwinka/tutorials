import random

value = random.random() # from 0 to 1 (non inclusive)
print(value)

value2 = random.uniform(1,10) # float random number from 1 to 10 (non inclusve)
print(value2)

value3 = random.randint(1,6) # integer number from 1 to 6 (inclusive)
print(value3)

greetings = ['Hello', "What's up", 'Hi', 'Hey']
value4 = random.choice(greetings) # take a random value from greetings
print(value4)

colors = ['Red', 'Black', 'Green']
value5 = random.choices(colors, weights=[5,5,1], k=10) # take a random value from colors and repiete it "k" times. Weights = chances. Non unic nums
print(value5)

deck = list(range(1, 53))
random.shuffle(deck) #shuffles deck
hand = random.sample(deck, k=2) # takes dack values "k" times
print(hand)
