def binwin():
    nn = input("Enter any Binary number [prefix it with 0b or 0B] : ")
    print(f"Given binary number {nn}'s decimal representation  : {int(nn,2)}")


def winbin():
    no = int(input("Enter any decimal number : "))
    print(f"Given decimal number {no}'s binary representation  : {bin(no)}")
   
winbin()

y = input("Enter y to continue for binary to decimal :")

if (y=="y"):
    binwin()
else:
    print("Program canceled")