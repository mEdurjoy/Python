square = lambda x: x**2
print(square(5))
print(square(10))
'''
def square(x):
    return x**2
'''

sum = lambda x, y: x + y
print(sum(5, 10))
print(sum(20, 30))
'''
def sum(x, y):
    return x + y
'''

avg = lambda x, y, z=0: (x + y + z) / 3
print(avg(5, 10, 15))
print(avg(30, 30))
'''
def avg(x, y, z):
    return (x + y + z) / 3 '''       