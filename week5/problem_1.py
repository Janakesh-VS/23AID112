class Student:
    def __init__(self):
        self.Id=100
        self.Name="Magesh"
        self.Location="Bangalore"
    
    def whoAmI(self):
        print("Id=",self.Id,"Name=", self.Name,"Location=", self.Location)
        
s1=Student()
s1.whoAmI()
s2=Student()
s2.whoAmI()
s3=Student()
s3.whoAmI()