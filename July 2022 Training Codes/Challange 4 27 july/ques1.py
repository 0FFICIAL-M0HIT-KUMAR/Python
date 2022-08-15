# # Write a python function which replaces all the vowels present in a string with @
# def replace_vowels(name):

#     vowels=["A","E","I","O","U","a","e","i","o","u"]

#     #string to list
#     name_list=[]
#     name_list[:0]=name

#     #replacing vowels character with @
#     for i in range(len(name_list)):
#         for j in range(len(vowels)):
#             if(name_list[i]==vowels[j]):
#                 name_list[i]="@"

#     #list to string
#     name_str=""
#     name=name_str.join(name_list)

#     return name

# name=input("Enter Your Word: ")
# print(replace_vowels(name))

# Write a python function which replaces all the vowels present in a string with @
def replace_vowels(name):

    #replacing vowels character with @
    for i in name:
        if i.lower() in ["a","e","i","o","u"]:
            name=name.replace(i,'@')
    return name


name=input("Enter Your Word: ")
print(replace_vowels(name))