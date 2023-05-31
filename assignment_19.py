#program using decorators
print("This is program using decorators")
'''
try:

    salary_L1 = 70000
    salary_L2 = 50000
    salary_L3 = 30000

    print(f"Salary of L1 Band before decoartor was {salary_L1}")
    print(f"Salary of L2 Band before decoartor was {salary_L2}")
    print(f"Salary of L3 Band before decoartor was {salary_L3}")

    #Legacy Function : 
    def salary_Bands(band):
        #print("in Salary Bands")
        if band == 'l1':
            #print("In Salary Band 1")
            print(f"Salary in L1 band is : {salary_L1}")
        elif band == 'l2':
            #print("In Salary Band 2")
            print(f"Salary in L2 band is : {salary_L2}")
        elif band == 'l3':
            #print("In Salary Band 3")
            print(f"Salary in L3 band is : {salary_L3}")
        else:
            print("Enter a valid band !")

    def bonus_Adder(func):
        def inner(band):
            if band == 'l1':
                global salary_L1  
                salary_L1 =  salary_L1 + 5000    
            elif band == 'l2':
                global salary_L2
                salary_L2 =  salary_L2 + 4000    
            elif band == 'l3':
                global salary_L3
                salary_L3 = salary_L3 + 3000    
            else:
                print(f"Entered {band} does not exist")
            return func(band)    
        return inner
    
    band = input("Enter salary band type (L1, L2, L3): ")
    band = band.lower()
    salary_Bands = bonus_Adder(salary_Bands)
    salary_Bands(band)

except BaseException as ex:
    print(ex)

'''


def updateName(func):
    def inner(first_Name, middle_Name, last_Name):
        first_Name = first_Name.capitalize()
        middle_Name = middle_Name.capitalize()
        last_Name = last_Name.capitalize()
        return func(first_Name, middle_Name, last_Name)
    return inner

@updateName
#Legacy Function
def printName(first_Name, middle_Name, last_Name):
    print("Your Full Name is :", first_Name + " " + middle_Name + " " + last_Name)


first_Name = input("Enter your First Name : ")
middle_Name = input("Enter your Middle Name : ")
last_Name = input("Enter your Last Name : ")

printName(first_Name, middle_Name, last_Name)