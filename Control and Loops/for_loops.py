for i in range(5):
    print(i)
#Another for loop example
print("Another for loop example:")
for i in range(1,5):
    print(i)

#Another for loop example
print("Another for loop example:")
for i in range(1,5):
    print("5 x",i,"=",5*i) 

#while loop example
print("While loop example:")
p=1
while p<5:
    print(p)
    p+=1
print("Now p is",p)

#while loop example with break
print("While loop example with break:")
p=1
while p<5:
    print(p)
    if p==3:
        break
    p+=1
print("Now p is",p)
