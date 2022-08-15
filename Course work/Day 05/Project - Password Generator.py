import random
letter_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S',
'T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p'
'q','r','s','t','u','v','w','x','y','z']
number_list = ['1','2','3','4','5','6','7','8','9','0']
symbol_list = ['!','@','#','$','%','&','*','?','+','-','/',]

print("Welcome to the Password Generator !")
pass_letter = int(input("How many letters would you like in your password ? \n"))
pass_symbols = int(input(f"How many symbols would you like ?\n"))
pass_number = int(input(f"How many number would you like?\n"))

# second try 
password = [] #for making list we use []
for i in range (0,pass_letter):
    random_generator = random.choice(letter_list)
    password += random_generator

for i in range (0,pass_symbols):
    random_generator = random.choice(symbol_list)
    password += random_generator

for i in range (0,pass_number):
    random_generator = random.choice(number_list)
    password += random_generator

# print(password)
random.shuffle(password)

shuffle_password = ""
for string in password:
    shuffle_password += string

print(shuffle_password)


# first try 
# password = ""
# # considering pass_letter = 4
# for char in range(0,pass_letter):
#     # letter=str(letter)
#     random_letter = letter_list[random.randint(0,52)]
#     password = password+random_letter
#     # password[letter] = random_letter

# # for symbol in range(0,pass_symbols):
# #     random_symbol = symbol_list[random.randint(1,10)]
# #     password = password+random_symbol

# # for num in range(0,pass_number):
# #     random_number = random.randint(0,9)
# #     password = password + str(random_number)
# print(password)

