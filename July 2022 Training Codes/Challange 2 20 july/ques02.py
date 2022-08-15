#Given a tuple of number (1,3,5,8,9,12,14). Create dictionary to display the cubes of number present in tuple as key value pairs.
given_tuple=(1,3,5,8,9,12,14)
#print(type(given_tuple))

convert_list=list(given_tuple)
# print(type(convert_list))


dic={}

for i in range (0,7):
    j=int(given_tuple[i])
    k=int((convert_list[i])*(convert_list[i])*(convert_list[i]))
    dic[j] = k
    
print(dic)

