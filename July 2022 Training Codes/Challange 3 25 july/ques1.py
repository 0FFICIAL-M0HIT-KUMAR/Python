#FACTORIAL PROGRAM n! = n*(n -1)!

def fact(n):
    if n!=0:
        for i in range (1,n):
            n=n*i
        return n
    else:
        return 1

numb = int (input ("\nEnter the number you want to get facrotial of that -> " ) )

print(f"\nFactorial of number {numb} is : {fact (numb)} \n" )