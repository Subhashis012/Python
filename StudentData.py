class Student:
    def __init__(self, name, marks): 
        self.name = name
        self.marks = marks
    @staticmethod    
    def hello():
        print("hello")
    def get_average(self):
        sum = 0
        for val in self.marks:
            sum+=val
        print("hi",self.name,"your avg score is: ",sum/3)    

s1 = Student("Subashis",[97,98,99]) 
s1.get_average()  
s1.name = "Moi"   
s1.hello()  