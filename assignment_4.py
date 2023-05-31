#Program to print using diffrent string formatting

print ("******PROGRAM FOR STRING FORMATTING ******")

#code for accepting details
f_Name = input ("Enter Your First Name : ")
l_Name = input ("Enter your Last Name : ")
_age = input("Enter your Age : ")

#code for string formatting 
print (f"My name is {f_Name} {l_Name} and my age is {_age}")     #use of F-string

print ("My name is {0} {1} and my age is {2}".format(f_Name,l_Name,_age))   #use of format method

print ("My name is",f_Name,l_Name,"and my age is",_age)     #simple string format 

print ("My name is %s %s and my age is %s"%(f_Name,l_Name,_age))    #use of % operator

print ("My name is " + (f_Name) + " " +(l_Name) + " and my age is " + _age)     #use of concatenation