#Program swapping of two numbers
from tempfile import tempdir


print("****** PROGRAM FOR SWAPPING OF TWO NUMBERS ******")
no_A = int (input ("Enter Fisrt Number : "))
no_B = int (input ("Enter Second Number : "))

#printing numbers
print ("\nNumbers Before swapping \n")
print ("Number A : ", no_A)
print ("Number B : ", no_B, "\n")

#logic for swapping
no_A , no_B = no_B , no_A
#temp = no_A
#no_A = no_B
#no_B = temp

#printing swapped numbers
print ("Numbers After swapping \n")
print ("Number A : ", no_A)
print ("Number B : ", no_B)