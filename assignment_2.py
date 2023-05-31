#Accept personal details and print in tabular form 

from texttable import Texttable

#code for accepting details
f_Name = input ("Enter first name : ")
l_Name = input ("Enter last name : ")
_dob = input ("Enter date of birth : ")
#m_NO = int(input("Enter contact number : "))    #add input pre declared
m_NO = int(8412046856)
e_Id = input ("Enter your E-mail address : ")

#code for tabular format
t = Texttable()
t.add_rows([['Name','last Name','DOB','Mobile Number','Mail ID'],[f_Name,l_Name,_dob,m_NO,e_Id]])
print (t.draw())
