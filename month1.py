Month=int(input("enter the month number:"))
'''30=1,3,5,7,8,10,12
31=4,6,9,11
28or 29=2'''
if(Month==1 or Month==3 or Month==5 or Month==7 or Month==8 or Month==10 or Month==12):
    print("31 days")
elif(Month==4 or Month==6 or Month==9 or Month==11):
    print("30 days")
elif(Month==2):
    print("28 or 29 days ")
else:
    print("in-valid month")          
