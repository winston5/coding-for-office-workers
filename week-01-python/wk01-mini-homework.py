import random
list = [1, 2, 3, 4, 5]
print(random.choice(list))

import random
list = [1, 2, 3, 4, 5]
print(random.sample(list,3))

import random
print(random.randint(1,5))

import random
print(random.randint(list[0],list[4]))

import random
from random import randint
countries = ["Korea", "Japan", "China", "USA", "Singapore"]
rand_index = randint(0,5)
print(countries[rand_index])

print(type(countries[rand_index]))
print(type(random.sample(countries,1)))
print(type(random.choice(countries)))

import random
flower = ["rose", "lily", "lavender"]
print(random.choice(flower))

import random
Africa = ["Zimbabwe", "Botswana", "South Africa", "Lethoso"]
Asia = ["Korea", "China", "Japan","Thailand"]
Europe = ["Germany", "France", "Switzerland", "France"]
America = ["USA", "Mexico", "Canada","Argentina"]

def whereto(continent):
    print(random.choice(continent))

whereto(Africa)
