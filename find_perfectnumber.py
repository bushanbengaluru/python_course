#program to find perfect number
num=int(input("Enter a number to check perfect number: ")) # input number
sum=0 #sum of divisors
div=1 #divisor
while div < num: #less than to exclude number itself
    if num % div == 0:
        sum = sum + div
    div = div + 1
if sum == num:
    print(div, "is a perfect number")
else:
    print(div, "is not a perfect number")
