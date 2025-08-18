'''
0 1 1 2 3 5 8 13 ....

'''

key=10

a=0 #0
b=1 #1
c=a+b #1
print(a,b,c,end=" ")
i=0 
while i<5:
    a=b #1
    b=c #1
    c= a+b #2
    print(c,end=" ")
    i+=1


