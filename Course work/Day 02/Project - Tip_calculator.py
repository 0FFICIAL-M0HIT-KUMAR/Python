print("Welcome to the tip calculator!")
bill=float(input("what was the total bill?\n "))
tip=int(input("How much tip would you like to give?\n 10, 12,or 15?\n"))
split=int(input("How many people to split the bill?\n"))
tip_percentage=tip/100*bill
total_bill=bill+tip_percentage
splitted_bill=total_bill/split
print(f"Each person should pay: ${splitted_bill}")