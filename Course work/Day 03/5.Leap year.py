year = int(input("Which year do you want to check? "))
four=year%4
if four==0:
   hundred=year%100
   if hundred==0:
       four_hundred=year%400
       if four_hundred==0:
           print("Leap year.")
       else:
            print("Not leap year.")
   else:
        print("Leap year.")
else:
    print("Not leap year.")