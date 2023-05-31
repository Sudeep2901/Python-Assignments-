#IF ELSE LADDER ASSIGNMENT
#Code to get Season at entered Month

print("Enter Month in short form 1.Jan 2.feb 3.mar 4.apr 5.may 6.jun 7.jul 8.aug 9.sep 10.oct 11.nov 12.dec ")

_month = input("Enter a month : ")
_month = _month.lower()

if _month == 'jan' or _month == 'feb' or _month == 'nov' or _month == 'dec':
    print(f"Season in Entered Month is winter")
elif _month == 'mar' or _month == 'apr' or _month == 'may' or _month == 'jun':
    print(f"Season in Entered Month is Summer")
elif _month == 'jul' or _month == 'aug' or _month == 'sep' or _month == 'oct':
    print(f"Season in Entered Month is Monsoon")
else:
    print("Enter a valid Month ")