class A:
    varA="welcome to class A"
class B:
    varB="welcome to class B "
class C(A,B):
    varC="welcome to class C"
obj=C()
print(obj.varA)
print(obj.varB)
print(obj.varC)