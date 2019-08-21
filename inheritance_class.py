class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Name : ",self.name)
        print("Age : ",self.age)
class Teacher(Person):
    def __init__(self,name,age,exp,r_area):
        Person.__init__(self,name,age)
        self.exp=exp
        self.r_area=r_area
    def displayData(self):
        Person.display(self)
        print("Experience : ",self.exp)
        print("RESEARCH AREA : ",self.r_area)
class Student(Person):
    def __init__(self,name,age,course,marks):
        Person.__init__(self,name,age)
        self.course=course
        self.marks=marks
    def displayData(self):
        Person.display(self)
        print("course : ",self.course)
        print("marks : ",self.marks)
print("*****************Teacher*****************")
T=Teacher("Avinash",43,20,"recommender system")
T.displayData()
print("*****************Teacher*****************")
S=Student("Mani",43,"Btech",75)
S.displayData()

