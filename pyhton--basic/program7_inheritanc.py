#this is single level inheritance

"""class A:
    def displayA(self):
        print("class A")
class B(A):
    def displayB(self):
        print("class B")
obj=B()
obj.displayB()
obj.displayA()"""

#this is multilevel inheritance

class A:
    def displayA(self):
        print("class A")
class B(A):
    def displayB(self):
        print("class B")
class C(B):  #another way of inherit is :::"class C(A,B):"
     def displayC(self):
        print("class c")

obj=C()
obj.displayC()
obj.displayB()
obj.displayA()