# class MyClass:
#     def __init__(self, attribute1, attribute2):
#         self.attribute1 = attribute1
#         self.attribute2 = attribute2

#     def method1(self):
#         print("Attribute 1:", self.attribute1)
#         print("Attribute 2:", self.attribute2)

#     def method2(self, parameter):
#         self.attribute1 += parameter
#         self.method1() 

# obj = MyClass("value1", "value2")
# obj.method1()
# obj.method2("updated_value")


class MyClass:
    def __init__(self, attribute1, attribute2):
        self.attribute1 = attribute1
        self.attribute2 = attribute2

    def method1(self):
        print("Attribute 1:", self.attribute1)
        print("Attribute 2:", self.attribute2)

    def method2(self, parameter):
        self.attribute1 += parameter
        self.method1() 

obj = MyClass("value1", "value2")
obj.method1()

obj.method2("updated_value")


