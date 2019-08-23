class Phone:
    def __init__(self,name,model_number):
        self.name=name
        self.model_number=model_number

    def fullName(self):
        return f"full name of {self.name}  {self.model_number}"

class Mobile(Phone):
    def __init__(self,name,model_number,price):
        super().__init__(name,model_number)
        self.price=price

    def fullName(self):
        return f"full name of {self.name} model is {self.model_number} price is {self.price}"

p=Phone('Nokia',1100)
print(p.fullName())
m=Mobile('Samsung','2019',400000)
print(m.fullName())
