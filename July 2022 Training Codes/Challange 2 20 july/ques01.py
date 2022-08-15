# # WAP to find maximum and minimum k elements in tuple and store all the values in a tuple.
input_tuple=input("Input some space seprated numbers : ")

input_tuple=input_tuple.split(" ")

size=len(input_tuple)

#changing from tuple to list
sorted_list=list(sorted(input_tuple))

print(sorted_list)

k=int(input("Enter the number of digits you want (minimum and maximum)"))
output=[]

if (k * 2 > size ):
    print("Not available because your tuple is so small for this")
else:
    for count,val in enumerate(sorted_list):
        if count < k or count >= size-k:
            output.append(val)

#further changing from list to tuple. But dont know why ?
output=tuple(output)
print("The extracted values : " + str(output))
