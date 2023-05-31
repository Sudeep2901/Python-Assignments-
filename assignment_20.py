'''
#Basic Class & Constructor  
print("***** Class & Constructor *****")
try:
    class employee:
        employeeName : str = ""
        employeeID : str = ""
        projectDet : str = ""
        def __init__(self):
            print("In Constructor")
            self.eName  = employeeName 
            self.eID = employeeID
            self.pDet = projectDet

        def showEmployeeData(self):
            print(f"Name is : {self.eName}")
            print(f"Employee ID is  : {self.eID}")
            print(f"Project Name is : {self.pDet}")
        
        def __del__(self):
            print("Object Destroyed")

    employeeName = input("Enter Your Name : ")
    employeeID = input("Enter Employee ID : ")
    projectDet = input("Enter Project Details : ")
    
    det = employee()
    det.showEmployeeData()

except BaseException as ex:
    print(ex)

class employee:
    def __init__(self,n,a,d):
        self.NA = n
        self.AG = a
        self.DB = d

    def printDet(self):
        print(f"NA IS : {self.NA}")
        print(f"DB IS : {self.DB}")
        print(f"AG IS :{self.AG}")

    def __del__(self):
        print("Destruction")

n = input("Enter n : ")
a = input("entr a : ")
d = input("enter d : ")
gg = employee(n,a,d)
gg.printDet()
'''

title = "Simple Class and Constructor Program"
print(title)

class details:
    def __init__(self,name,age):
        self._name = name
        self._age = age

    def showDetails(self):
        print(f"Name is {self._name}")
        print(f"Age is {self._age}")

name = input("Enter Your Name : ")
age = input("Enter your Age : ")
me = details(name,age)
me.showDetails()

