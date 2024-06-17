#Understanding of Inheritance in class

class Person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        self.item  = {}
    
    def add_item(self,key,value):
        self.item[key] = value

    def printClass(self):
        print(f"Name: {self.fname} {self.lname},\nDetails:\t\n {self.item}")


class Student(Person):
    ''' if we define child class __init__ then parent class __init__ inheritance will not work so for that we can do that this way '''
    
    def __init__(self,fname,lname):
        Person.__init__(self,fname,lname)
        ''' we can modify the function here also'''
        self.age = 10

# taking an instance of the class

#taking normal class 
Astudent = Student("Dipankar","Mandal")
Astudent.printClass()
#adding a new item in class instance 
Astudent.add_item("DOB","05-04-1998")
Astudent.printClass()

Astudent.add_item("Gender","M")
Astudent.printClass()

Astudent.add_item("age","10")
Astudent.printClass()
