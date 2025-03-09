def find_isprime(check_num):
        for i in range(2, check_num):
            if check_num % i == 0:
                return "Number is not prime"
                break
        else:
            return "Number is prime"    
print("Program to find if given number is prime number")
prime_nums = []
check_num = int(input("Enter number: "))
res = find_isprime(check_num)
print(res)