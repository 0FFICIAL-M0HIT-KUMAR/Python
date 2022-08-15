print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1=name1.lower()
name2=name2.lower()
name=name1+name2

count_true=int(name.count("t"))
count_true+=int(name.count("r"))
count_true+=int(name.count("u"))
count_true+=int(name.count("e"))

count_love=int(name.count("l"))
count_love+=int(name.count("o"))
count_love+=int(name.count("v"))
count_love+=int(name.count("e"))

score=int(str(count_true)+str(count_love))

if score<10 or score>90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score>=40 and score<=50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score},You made for each other.")
