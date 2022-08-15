#CHECKING THE NUMBER IS EVEN OR ODD

def check_num(n):

    if (n%2==0):

        print(f"{n} Number is even")

    else:

        print(f"{n} Number is odd")

number=int(input("Enter your number -> \n"))

check_num(number)