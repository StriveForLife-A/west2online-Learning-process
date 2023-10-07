class Goods():
    def __init__(self,id,name,price,total,remain):
        self.id=id
        self.name=name
        self.price=price
        self.total=total
        self.remain=remain

    def display(self):
        print(f"{self.name},序号{self.id},单价{self.price}元,总共{self.total}个，剩余{self.remain}个。")

    def income(self):
        income=(self.price*(self.total-self.remain))
        print(f"收入：{income}元")

    def setdata(self,id,name,price,total,remain):
        self.id=id
        self.name=name
        self.price=price
        self.total=total
        self.remain=remain

mango=Goods(1001,"芒果",5,100,10)
watermelon=Goods(1002,"西瓜",5,50,15)
apple=Goods(1003,"苹果",5,50,10)
banana=Goods(1004,"香蕉",5,100,30)



mango.display()
mango.income()
watermelon.display()
watermelon.income()
apple.display()
apple.income()
banana.display()
banana.income()
