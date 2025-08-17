a = 24
b=2
#Arithmetic operations
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a % b =", a % b)
print("a // b =", a // b) 

#Conditional operations
print("---Conditional Operations---")
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

#Logical operations
print("---Logical Operations---")
m = True
n = False
print(True and True)
print(True and False)
print(False and True)
print(False and False)

print(True or True)
print(True or False)
print(False or True)
print(False or False)

print(not True)
print(not False)

#Assignment operations
print("---Assignment Operations---")
a = 10
print("a =", a) 
a += 5
print("a after += 5:", a)
a -= 3  
print("a after -= 3:", a)
a *= 2
print("a after *= 2:", a)
a /= 4
print("a after /= 4:", a)
print(a)
print("a after %= 3:", a % 3)
print("a after //= 2:", a // 2)
print("a after **= 2:", a ** 2)

#Membership operations
print("---Membership Operations---")
my_list = [1, 2, 3, 4, 5]
print(3 in my_list)
print(3 not in my_list)
print("Hello" in "Hello, World!")

#Identity operations
print("---Identity Operations---")
x = [1, 2, 3]
y = x
print(x is y)  # True, same object
print(x is not y)  # False, same object