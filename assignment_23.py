#Petrol Pump Simulation
import fuelRates as fr

print("****** Welcome to Petrolium ******")

def petrol_Calculator(amount):
    fill = amount/fr.petrol
    return fill

def diesel_Calculator(amount):
    fill = amount/fr.diesel
    return fill

def cng_Calculator(amount):
    fill = amount/fr.cng
    return fill

ch = input("Enter Fuel type of your vehicle : \n1]Petrol\n2]Diesel\n3]CNG : ")
if ch == '1':
    print("***** Petrol *****")
    print(f"Petrol Rate = Rs.{fr.petrol}/ltr")
    amount = float(input("Enter Amount to fill : Rs."))
    print(f"Petrol Filled = {petrol_Calculator(amount)} ltr")

elif ch == '2':
    print("***** Diesel *****")
    print(f"Diesel Rate = Rs.{fr.diesel}/ltr")
    amount = float(input("Enter Amount to fill : Rs."))
    print(f"Diesel Filled = {diesel_Calculator(amount)} ltr")

elif ch == '3':
    print("***** CNG *****")
    print(f"CNG Rate = Rs.{fr.cng}/Kgs")
    amount = float(input("Enter Amount to fill : Rs."))
    print(f"CNG Filled = {cng_Calculator(amount)} Kgs")

else:
    print("Enter a valid choice !")