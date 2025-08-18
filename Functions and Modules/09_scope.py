def add(x, y):
    '''
    Here the addition of two numbers is performed.
    '''
    return x + y

def subtract(x, y):
    global p
    p=190
    return x - y

x=5
p=45
print(add(4, 10))
print(subtract(10, 4))
print(x)
print(p) #this is the global variable