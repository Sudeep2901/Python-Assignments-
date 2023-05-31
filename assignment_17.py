#program using Lambda Functions

try:
    def calci():
        print("******Calculator Program*******")
        print("Enter choice for calculations : ")
        print("1.Addition\n2.Substraction\n3.Multiplication\n4.Division")
        choice  = int(input("Enter choice : "))
        if choice == 1:
            print("******Addition******")
            no1 = int(input("Enter first num : "))
            no2 = int(input("Enter second number :"))
            addition = lambda number1, number2 : number1+number2
            print(f"Answer : {addition(no1,no2)}") 
        elif choice == 2:
            print("******Substraction******")
            no1 = int(input("Enter first num : "))
            no2 = int(input("Enter second number :"))
            substraction = lambda number1, number2 : number1-number2
            print(f"Answer : {substraction(no1,no2)}") 
        elif choice == 3:
            print("******Multiplication*****")
            no1 = int(input("Enter first num : "))
            no2 = int(input("Enter second number :"))
            multiplication = lambda number1, number2 : number1*number2
            print(f"Answer : {multiplication(no1,no2)}") 
        elif choice == 4:
            print("*****Division******")
            no1 = input("Enter first num : ")
            no2 = input("Enter second number :")
            division = lambda number1, number2 : number1/number2
            print(f"Answer : {division(no1,no2)}")    
        else:
            print("Enter a valid Choice !")   

    while (True):
        calci()
        cont = input("Enter do you want to continue [y/n] : ")
        if cont !='y':
            break

except BaseException as ex:
    print(ex)