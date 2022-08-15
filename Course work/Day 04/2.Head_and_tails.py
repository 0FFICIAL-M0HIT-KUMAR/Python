import random

# Taking input in test seed 
test_seed = int(input("Create a seed number: "))

#Line 7th code is nothing , its just response of the input so that program can run further.
random.seed(test_seed)

if test_seed > 0 :
    random_integer = random.randint(0,1)
    if random_integer==0:
        print("Tails")
    else:
        print("Heads")
else:
    print("you chooses wrong number")