#Program swapping of my name 
print("****** PROGRAM FOR SWAPPING OF NAME ******")
f_Name = input ("Enter Fisrt Name : ")
l_Name = input ("Enter Last Name : ")

#printing Name 
print ("\nName Before swapping \n")
print ("First Name to be printed : ", f_Name)
print ("Last Name to be printed: ", l_Name, "\n")

#logic for swapping
f_Name , l_Name = l_Name , f_Name

#printing swapped numbers
print ("Name After swapping \n")
print ("first Name after swapping : ", f_Name)
print ("Second Name after swapping : ", l_Name)