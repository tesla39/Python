"""class class1:
    a=10
    def function1(this):
        print(20+1)
obj=class1()
print(obj.a)
obj.function1()"""

"""class class2:
    a=20
    def function1(this):
        print(this.a)
        this.var=5
        print(this.var)
obj=class2()
obj.function1()"""

class class3:
    def function2(self,a,b):
        self.c=a+b
        return self.c
obj=class3()
ans=obj.function2(3,4)
print(ans)

    