#Write a python function to find the point of intersection of two linear equations which two variables (x and y)
# The program progression should be like this ...
#Program ask 1st equation like enter first equation : ax+by+c=0
#Program ask 2nd equation like enter first equation : lx+my+p=0
#Point of intersection of the equations : __answer__

equation_one = input("Enter 1st Equation : ")
eone = []
for z in equation_one.split():
   if z.isdigit():
      eone.append(int(z))
# print("Find number in string:",eone)

equation_second = input("Enter 1st Equation : ")
esecond = []
for z in equation_second.split():
   if z.isdigit():
      esecond.append(int(z))

# print("Find number in string:",esecond)

a,b,c,l,m,p=eone[0],eone[1],eone[2],esecond[0],esecond[1],esecond[2]

x=int((b*p-m*c)/(a*m-l*b))
y=int((l*c-a*p)/(a*m-l*b))

print(x,y)