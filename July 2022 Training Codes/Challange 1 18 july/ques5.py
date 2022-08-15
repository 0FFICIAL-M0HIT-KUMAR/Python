# Q5: Write a program to print all the elements of array using for and while loop.
array=["a","b","c","d","e","f","g",]

print("FOR LOOP IMPLEMENTATION ->")
for i in range(0,len(array)):

    print(array[i])

print("\n")

print("WHILE LOOP IMPLEMENTATION ->")
i=0
while(i!=len(array)):
    print(array[i])
    i+=1