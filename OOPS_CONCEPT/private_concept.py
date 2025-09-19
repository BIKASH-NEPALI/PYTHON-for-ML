class Account:
    def __init__(self,acc_no,psswrd):
        self.acc_no=acc_no
        self.__psswrd=psswrd
acc1=Account("12345","abcde")
print(acc1.acc_no)
print(acc1.__psswrd)
