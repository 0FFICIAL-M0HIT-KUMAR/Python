# Q2:  Write a program to iterate the first 10 numbers and in each
# iteration, print the sum of the current and previous number.
# Output will be like --> 
# Current number and previous number sum in range (10)
# Current number 0 Previous Number 0 Sum: 0
# Current number 1 Previous Number 0 Sum: 1
# Current number 2 Previous Number 1 Sum: 3 and so on 

cn=int(0)
pn=int(0)
sum=int(0)


for i in range(10):
    pn=cn
    cn=i
    sum=cn+pn
    print(f"Current Number {cn} Previous Number {pn} sum : {sum}")

