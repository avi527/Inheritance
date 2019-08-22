class Hero:
    def __init__(self,model,price,cc):
        self.model=model
        self.price=price
        self.cc=cc
    def bikeDiscription(self):
        return f"model name : {self.model}  price {self.price}  {self.cc}"

class Passionpro(Hero):
    def __init__(self,model,price,cc,name):
       super().__init__(model,price,cc)
       self.name=name
    def bikeName(self):
        return f"bike name is {self.name}"

class Glamour(Hero):
    def __init__(self,model,price,cc,name,color,manufacture_date):
        super().__init__(model,price,cc)
        self.manufacture_date=manufacture_date
        self.color=color
    def extraDiscription(self):
        return f"manufacture date is {self.manufacture_date} and color is {self.color}"
    def allDiscriptionOfGlamour(self):
        return f"model is {self.model} \n and price is {self.price} and cc is {self.cc} and"

bike=Hero('2017',45000,'100 cc')
print(bike.bikeDiscription())
passionpro=Passionpro("2018",60000,'125cc','Passion Pro')
print(passionpro.bikeName())
glamour=Glamour("2018",60000,'125cc','Passion Pro','red','20/03/2019')
print(glamour.extraDiscription(),glamour.cc,glamour.price)
print(glamour.allDiscriptionOfGlamour())



