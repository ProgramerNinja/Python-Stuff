##Jared M.
##1/17/19


class Bank_acc(object):
    def __init__(self):
        self.name=""
        self.balance = 0
        self.pin = 1234
        self.intrate = 0.06
        self.acc_num = 123456789
    def credit_acc(self):
        amount = float(input("enter your deposit: "))
        self.balance+=amount
    def debit_acc(self):
        get_pin = int(input("what is your pin: "))
        if get_pin != self.pin:
            print("that is not correct, the cops have been notified")
        else:
            amount = float(input("enter your withdrawl: "))
            self.balance-=amount

par_acc=Bank_acc()
par_acc.name = "Parker"
print(par_acc)
par_acc.credit_acc()
print(par_acc.balance)
par_acc.debit_acc()
print(par_acc.balance)