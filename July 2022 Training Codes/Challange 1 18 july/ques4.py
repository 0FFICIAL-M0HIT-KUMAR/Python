#Q4: Print the numbers from 256 and 398 that are divisible by 17
for i in range (256,398):
    if(int(i%17)==0):
        print(f"Divisible by 17 are : {i}")
