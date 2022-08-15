# string 
def s(li):
  mstr=" "
  mlist=list(li)
#   print(mlist)
  for i in range (0,len(mlist)):
    if(i%2==0):
     mlist[i]="$"
  
  print(mstr.join(mlist))

str=input("Enter your string")
s(str)