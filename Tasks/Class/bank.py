class Bank:
    def __init__(self, name, acc_no, amount):
        self.__name = name
        self.__acc_no = acc_no
        self.amount = amount
    def info(self):
        return self.__name, self.__acc_no, self.amount

name = str(input("Enter name: "))
acc_no = int(input("Enter account number: "))
amount = int(input("Enter amount: "))
b = Bank(name, acc_no, amount)
res = b.info()
print("{} has account number {} and amount is {}".format(res[0], res[1], res[2]))
# Private access modifier:
b.name="Ramesh" #Trying to modify name
res=b.info()
print("{} has account number {} and amount is {}".format(res[0], res[1], res[2]))