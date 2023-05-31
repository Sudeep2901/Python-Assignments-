_name = input ("Enter name : ")
_mob = input ("Enter mobile number : ")
#_email = input ("Enter E- mail ID : ")

if (_name.isalpha()==True and _mob.isnumeric()==True):
    print(" Format accepted !")
else :
    print("format invalid !")

a="sudeep.kulkarni@gmail.com"
lst=list()
for ltr in a:
    lst.append(ltr)
#print(lst)
y=1
for i in (lst):
    if i=="@":
        y+=1
        if(y==2):
            print("email accepted")
    else:
        continue
if(y==1):
    print('Not email')
