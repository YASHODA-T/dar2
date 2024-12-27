'''a=int(input("enter the 1st integer value:"))
b=int(input("enter the 2nd integer value:"))
if(a==b):
    print("two integers are eqal")
else:
    print("two integers are not eqal7")
print("------------------------------------")  
a=int(input("enter the first integer value:"))
b=int(input("enter the second integer value:"))
Result="two integers are eqal" if(a==b) else "given integers are not eqal"  
print(Result)'''
# find the greatest number inputs
'''a=int(input("enter the 1st integer:"))
b=int(input("enter the 2nd integer:"))
greatest=max(a,b)
print(greatest)'''
#find the smallest number
'''a=int(input("enter the 1st integer:"))
b=int(input("enter the 2nd input:"))
smallest=min(a,b)
print(smallest)'''
#find middle value
a=int(input("enter the 1st element:"))
b=int(input("enter the 2nd integer:"))
c=int(input("enter the 3rd integer value:"))
if((b>a and c<a) or (a>c and b<a)):
    print("a is middle value")
elif((b>a and b<c) or (b>c and b<a)):
    print("b is middle value")
else:
    print("c is middle valuev")