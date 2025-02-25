def find_prime(start, end):
    y = []
    for num in range(start, end):
        for i in range(2, num):
            if num % i == 0:
                break
            else:
                y.append(num)
                break
    return y
print("Program to find prime numbers from given range of start and end number")
start = int(input("Enter start number: "))
end = int(input("Enter end number: "))
for a in find_prime(start,end):
    print(a, end=' ')