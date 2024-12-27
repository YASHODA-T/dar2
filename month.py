'''month=int(input("enter the month number:"))
if(month>=1 and month<=12):
    print("it is valid")
else:
    print("in-valid")'''
Month=int(input("Enter the Month number:"))
Result="Valid Month Number" if(Month%2==0) else "In-Valid Month Number"
print(Result)