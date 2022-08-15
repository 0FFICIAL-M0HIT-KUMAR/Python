# Create a list which has tuples of different lenghts as elements.

list_is = [(1,2,3),(1,2,3,4),(1,2,3,4,5),(1,2,3,4,5,6,8),(1,2,5,3,8,4)]

list_is.sort(key=len,reverse=True)

print(list_is)

