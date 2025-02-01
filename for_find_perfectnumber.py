#program to find perfect number between 1 to 1000
for num in range(1, 1000): #
    sum=0
    for newnum in range(1, num):
        if num%newnum==0:
            sum=sum+newnum
    if sum == num:
        print(sum)