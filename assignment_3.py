#Program for writing file level docstring
'''
Name : Sudeep Uday Kulkarni
Date : 15 - 10 - 2022
Description : Assignment for writing docstring at file level
'''
print (__doc__)
print ("****** PROGRAM FOR DOCSTRING ******")
#Docstring in a Function
def myFunction():
    '''
    Description : Docstring in a Function
    '''
print (myFunction.__doc__)    
#Docstring in a Class
class myClass:
    '''
    Description : Docstring in a class
    '''
print (myClass.__doc__)    
