Rock=(
"""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

Paper =(
"""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

Scissors=(
"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

Image=[Rock, Paper, Scissors]
import random
print("WELCOME TO ROCK PAPER AND SCISSOR GAME ! Lets play...")
print("what do you want to choose ?")

Your_decision = int(input("Type 0 for Rock , 1 for Paper and 2 for Scissor \n"))
if Your_decision > 2:
    print("Invalid Input ! You Loose")
else:
    print(Image[Your_decision])
    
    print("Computer Choosen")
    Computer_decision = random.randint(0,2)
    print(Image[Computer_decision])

    if Your_decision==Computer_decision:
        print("DRAW")
    elif Your_decision==1 and Computer_decision==0:
        print("You Win")
    elif Your_decision==2 and Computer_decision==1:
        print("You Win")
    elif Your_decision==0 and Computer_decision==2:
        print("You Win")
    else:
        print("You Loose")