print("Welcome to the rollercoaster!")

height = int(input("what is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age=int(input("what is your age? "))

    if age<12:
        Bill=5
        print("Child Ticket are 5$")

    elif age <= 18:
        Bill=7
        print("Youth Ticket are 7$")

    else:
        Bill=12
        print("Adult Ticket are 12$")

    photo = input("Do you want to get photos? Y / N : ")

    if photo=="Y":
        Bill+=3
        print("Your Bill is "+str(Bill)+("$"))
        
    print("Your Bill is "+str(Bill)+("$"))

else:
    print("Sorry,you have to grow taller before you can ride.")