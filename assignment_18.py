#Program to calculate Rate of interest amount

c_Interest = 8.25
h_Interest = 9
e_Interest = 7.50
p_Interest = 8.50

try:
    while (True):
        print("*****LOAN INTEREST CALCULATOR*****")

        principle_amount = float(input("Enter Loan Amount : "))
        tenure = float(input("Enter tenure in years : "))

        print("Select Type of Loan : \n1.Car Loan\n2.Home Loan\n3.Education Loan\n4.Personal Loan")
        choice = int(input("Enter Your loan type : "))
        if choice == 1:
            print("****Car Loan****")
            interest_c = lambda p,n,r : (p*n*r)/100
            totalIntAmount = interest_c(principle_amount,tenure,c_Interest)
            monthly_amount = lambda a,b: a/(b*12)
            monthlyIntAmount = monthly_amount(totalIntAmount,tenure)
            print(f"Total Interest on Loan : {totalIntAmount}")
            print(f"Total Interest to be paid in every Month : {monthlyIntAmount}")
            print(f"Total Loan Amount : {principle_amount + totalIntAmount}")
            print(f"Total Amount to be paid on every month : {monthlyIntAmount+(principle_amount/(tenure*12))}")

        elif choice == 2:
            print("****Home Loan****")
            interest_h = lambda p,n,r : (p*n*r)/100
            totalIntAmount = interest_h(principle_amount,tenure,h_Interest)
            monthly_amount = lambda a,b: a/(b*12)
            monthlyIntAmount = monthly_amount(totalIntAmount,tenure)
            print(f"Total Interest on Loan : {totalIntAmount}")
            print(f"Total Interest to be paid in every Month : {monthlyIntAmount}")
            print(f"Total Loan Amount : {principle_amount + totalIntAmount}")
            print(f"Total Amount to be paid on every month : {monthlyIntAmount+(principle_amount/(tenure*12))}")

        elif choice == 3:
            print("****Education Loan****")
            interest_e = lambda p,n,r : (p*n*r)/100
            totalIntAmount = interest_e(principle_amount,tenure,e_Interest)
            monthly_amount = lambda a,b: a/(b*12)
            monthlyIntAmount = monthly_amount(totalIntAmount,tenure)
            print(f"Total Interest on Loan : {totalIntAmount}")
            print(f"Total Interest to be paid in every Month : {monthlyIntAmount}")
            print(f"Total Loan Amount : {principle_amount + totalIntAmount}")
            print(f"Total Amount to be paid on every month : {monthlyIntAmount+(principle_amount/(tenure*12))}")
            
        elif choice == 4:
            print("****Personal Loan****")
            interest_p = lambda p,n,r : (p*n*r)/100
            totalIntAmount = interest_p(principle_amount,tenure,p_Interest)
            monthly_amount = lambda a,b: a/(b*12)
            monthlyIntAmount = monthly_amount(totalIntAmount,tenure)
            print(f"Total Interest on Loan : {totalIntAmount}")
            print(f"Total Interest to be paid in every Month : {monthlyIntAmount}")
            print(f"Total Loan Amount : {principle_amount + totalIntAmount}")
            print(f"Total Amount to be paid on every month : {monthlyIntAmount+(principle_amount/(tenure*12))}")

        else:
            print("Enter a valid choice !")
            interest_c = lambda p,n,r : (p*n*r)/100
            totalIntAmount = interest_c(principle_amount,tenure,c_Interest)
            monthly_amount = lambda a,b: a/(b*12)
            monthlyIntAmount = monthly_amount(totalIntAmount,tenure)
            print(f"Total Interest on Loan : {totalIntAmount}")
            print(f"Total Interest to be paid in every Month : {monthlyIntAmount}")
            print(f"Total Loan Amount : {principle_amount + totalIntAmount}")
            print(f"Total Amount to be paid on every month : {monthlyIntAmount+(principle_amount/(tenure*12))}")

        cont = input("Do you want to continue (y/n): ")
        if cont != 'y':
            break

except BaseException as ex:
    print(ex)