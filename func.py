class Calc:
    num = 100

    def __init__(self,a,b):
        self.a=a
        self.b=b
        print("auto called")

    def getData(self):
        print("I am now executing as method in class")

    def sus(self):
        return self.a + self.b

obj = Calc(4, 5)
obj.getData()
print(obj.num)
print(obj.sus())
