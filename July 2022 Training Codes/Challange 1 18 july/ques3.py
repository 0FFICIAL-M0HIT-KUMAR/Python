# Program to print the odd number and even number that falls between 156 and 317.
for i in range(156,319):
    if(i%2==0):
        even=i
    elif(i%2!=0):
        odd=i
        print(f"Even number is : {even} Odd number is :{odd}")