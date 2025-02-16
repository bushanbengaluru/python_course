#program to find perfect number
num=1
while num < 1000: #less than to exclude number itself
    div = 1
    sum = 0 #initialize sum
    while div < num:
        if num % div == 0:
            sum = sum + div
        div = div + 1
    num = num + 1
if sum == num:
    print(div, "is a perfect number")
else:
    print(div, "is not a perfect number")
