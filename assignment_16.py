#Simple Menu Driven Program
print(__doc__)
print("** Simple Menu driven Program **")
while True:
    print("Enter Choice For Conversion of : ")
    print("1. C to F\n2. F to C")
    choice = int(input("Enter Choice : "))
    if choice == 1:
        C = float(input("Enter temperature in C : "))
        cf = (C*(9/5))+32
        print(f"{C} C in farenheit is : {cf}")
    elif choice ==2:
        F =float(input("Enter temperature in F : "))
        fc = ((F)-32)*(5/9)
        print(f"{F} F in Celsius is : {fc}")
    else:
        print("Enter Valid Choice")
    ans = input("Do you want to contine (y/n):")
    ans = ans.lower()
    if ans!='y':
        break