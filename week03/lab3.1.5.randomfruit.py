# This program prints out a random fruit

import random

fruits = ('apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape')
# we want a random number between 0 and length -1
index = random.randint (0, len(fruits) -1)

fruit = fruits [index]
print("A random fruit: {}" .format(fruit))