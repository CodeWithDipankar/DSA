#Basic class Initiating ---

class Person:
    def __init__(self,fName,lName):
        self.fName = fName
        self.lName = lName
    
    def printPerson(self):
        print(f"Person name is: {self.fName} {self.lName}")


#Taking a instance of the class
APerson = Person("Dipankar","Mandal")
APerson.printPerson()