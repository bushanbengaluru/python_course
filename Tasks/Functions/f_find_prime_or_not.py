def find_isprime(check_num):
        if check_num % i == 0:
            return(i)
print("Program to find if given number is prime number")
prime_nums = []
check_num = int(input("Enter number: "))
i = 1
while i < check_num+1 :
    if find_isprime(i) is True:
        prime_nums.append(i)
    i += 1
print(prime_nums)