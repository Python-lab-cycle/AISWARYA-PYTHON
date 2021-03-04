class Bank():
    def __init__(self, acnt, nam, typ, amt):
        self.ac = acnt
        self.name = nam
        self.type = typ
        self.amount = amt

    def printamnt(self):
        print("Acc Name: ", self.name)
        print("Acc Number: ", self.ac)
        print("Acc Type: ", self.type)
        print("Amount: ", self.amount)

    def withdraw(self, w1):
        return(self.amount-w1)


n = input("Enter Your Name: ")
t = input("Enter Acc Type: ")

a = int(input("Enter Acc Number: "))
am = int(input("Enter Amount: "))
obj = Bank(a, n, t, am)
print("Account Details")
obj.printamnt()
w = int(input("Enter Amount to Withdraw: "))
print("Balance= ", obj.withdraw(w))
