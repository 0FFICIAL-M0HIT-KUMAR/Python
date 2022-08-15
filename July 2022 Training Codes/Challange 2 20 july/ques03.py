# Create a list which has 5 tuples as element as [(),(),(),(),()]. Then write a code to find all the
# tuples in the list which has length 5 and delete the rest of the tuples.
list_is = [(1,2,3),(1,2,3,4),(1,2,3,4,5),(6,7,8,9,10),(1,2,3,4,5,6,8),()]

print("DISPLAYING THE TUPLES IN LIST ONE BY ONE")
for i in range (len(list_is)):
    print(list_is[i])

print("\nDISPLAYING THE TUPLE OF LENGHT 5")
for i in range (len(list_is)):
    if(len(list_is[i]) == 5):
        print(list_is[i])
    else:
        i=i+1

print("\nDISPLAYING THE REST TUPPLES IN LIST")
for i in range (len(list_is)):
    if(len(list_is[i]) != 5):
        print(list_is[i])
    else:
        i=i+1

modify_list=[]
#DELETING THE TUPLE
for i in range (len(list_is)):
    if(len(list_is[i]) == 5):
        modify_list.append(list_is[i])
    else:
        i=i+1

# m_list= tuple(modify_tupple)
print("\nMODIFIED LIST IS ")
print(modify_list)
