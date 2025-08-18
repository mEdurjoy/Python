def fib(n):
    if n==0 or n==1:
        return n
    return fib(n-1) + fib(n-2)

for i in range(10):
    p=fib(i)
    print(p,end=" ")
print()

for i in range(30):
    p=fib(i)
    print(p,end=" ")
print()