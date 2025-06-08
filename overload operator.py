class A:

    def __init__(self, a):
        self.a = a

    def __lt__(self, other):
        return self.a < other.a

    def __eq__(self, other):
        return self.a == other.a

ob1 = A(2)
ob2 = A(3)
print("Passed Values: ", ob1.a, ob2.a)

if ob1 < ob2:
    print("ob1 is less than ob2")
else:
    print("ob2 is less than ob1")

ob3 = A(4)
ob4 = A(4)
print("Passed Values :", ob3.a, ob4.a)

if ob3 == ob4:
    print("Both are equal")
else:
    print("Not Equal")