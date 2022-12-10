def leapyear(x):
    if(x%4==0 and x%100!=0 or x%400==0):
        return True
    else:
        return False
    
def nonleapyear(x):
    if(x%4!=0 or x%100==0 and x%400!=0):
        return True
    else:
        return False
    
x=int(input("Enter the starting year:"))
y=int(input("Enter the ending year:"))
print("\n")
print("Leap Year::",end=' ')
for i in range(x,y+1):
    if(leapyear(i)==True):
        print(i,end=' ')
        

print("\n")
print("Non Leap Year::",end=' ')
for j in range(x,y+1):
    if(nonleapyear(j)==True):
        print(j,end=' ')
        
print("\n")
