# Importing the library which is pre-built in python library
import random

# taking variable as random_integer
# calling the function (randint) of library random
random_integer = random.randint(1,10)
# printing random_integer
print(random_integer)

# importing another own module named as 1.1 part of random demo .py
import part_of_frst_one

# taking values from our own module like this 👇
print(part_of_frst_one.pi)

# making random float number
random_float = random.random()
print(random_float)

# if we want to increase the limit from 0-1
# it will be done like this 👇
big_float_limit = random_float*85
print(big_float_limit)