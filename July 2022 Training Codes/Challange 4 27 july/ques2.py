# #Write a python function which finds whether the number belongs to fibonacci series
# def get_fibonacii(n):
#     a,b,c=0,1,2

#     fibo_series=[a,b]

#     while c<=n:
#         fibo=a+b
#         fibo_series.append(fibo)
#         a=b
#         b=fibo
#         c=c+1

#     return fibo_series

# #How many elements you want to enter 👇
# range_number=int(input("Enter the number of elements: "))
# fibonacii_series=get_fibonacii(range_number)

# #Which number do you want to check 👇
# validation_number=int(input("Enter the number do you want to check : "))

# for i in range (len(fibonacii_series)):
#         if fibonacii_series[i]==validation_number:
#             here="true"
#             break
#         else:
#             here="false"

# if (here=="true"):
#     print(f"Number {validation_number} is in fibonacci series")
# else:
#     print(f"Number {validation_number} is not in fibonacci series")
    
def findInFibonacci(num):
    f0 = 0
    f1 = 1
    
    while(f1 + f0 <= num):
        f1 += f0
        # print(f1)
        f0 = f1 - f0
        # print(f1)
        
    if f1 == num:
        print("%s is present in fibonacci series" %(num))
        
    else:
        print("%s is not present in fibonacci series" %(num))

findInFibonacci(32)