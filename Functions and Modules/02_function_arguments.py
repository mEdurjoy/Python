'''
Type of Arguments
1. Positional Arguments 
2. Keyword Arguments
3. Default Arguments
4. Variable-length Arguments
'''
print("----------Default Arguments----------")
def avg_return(a,b,c=0):
    return (a+b+c)/3
o1 = avg_return(5,2)
o2 = avg_return(4,5,6)
print(o1)
print(o2)

print("----------Keyword Arguments----------")
def avg_return(b,a,c=0):
    return (a+b+c)/3
o1 = avg_return(a=5,b=2)
o2 = avg_return(b=4,a=5,c=6)
print(o1)
print(o2)