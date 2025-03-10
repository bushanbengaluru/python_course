def finding_series(func):
    def inner_series():
        func()
        y = []
        for num in range(1, check_num):
            for i in range(2, check_num):
                if num % i == 0:
                    break
                else:
                    y.append(num)
                    break
        print(y)
    return inner_series


def decorator_func(func):
    def inner_func():
        res = func(check_num)
        print(res)
    return inner_func

@finding_series
@decorator_func
def find_isprime(check_num):
        for i in range(2, check_num):
            if check_num % i == 0:
                return "Number is not prime"
            else:
                return "Number is prime"    

print("Program to find if given number is prime number")
check_num = int(input("Enter number: "))
find_isprime()