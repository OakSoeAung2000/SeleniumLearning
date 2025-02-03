from func import Calc


class ChildImpl(Calc):
    num2 = 200

    def __init__(self):
        Calc.__init__(self, 2, 10)

        
    def getComp(self):
        return self.num2 + self.sus()

obj = ChildImpl()
print(obj.getComp())