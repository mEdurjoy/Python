def fib(n):
    if(n==0 or n==1):
        return n
    return fib(n-2) + fib(n-1)


print(fib(3))
print(fib(4))
print(fib(18))
print(fib(30))
