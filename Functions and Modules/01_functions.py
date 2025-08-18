
#Function 
def avg(a,b,c):
    print((a+b+c)/3)

avg(1,2,3)
avg(4,5,6)

print("----------Function with return type----------")
def avg_return(a,b,c):
    return (a+b+c)/3
o1 = avg_return(1,2,3)
o2 = avg_return(4,5,6)
print(o1)
print(o2)