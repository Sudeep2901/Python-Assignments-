'''
i=1                        #line 1
while(i<=5):               #line 2
    j=5                    #line 3
    while(j>=i):           #line 4
        print(j, end=' ')  #line 5
        j-=1               #line 6
        i+=1                   #line 7
    print()                #line 8
''' 
rows = 6 
for i in range (0, rows):
    for j in range (rows - 1,i,-1):
        print(j,"",end = "")
    for l in range (i):
        print("   ", end = "")
    for k in range (i+1,rows):
        print(k,"",end = "")
    print("\n")