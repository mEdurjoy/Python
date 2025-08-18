def fibonacci(n):
    a=0
    b=1
    c=a+b
    if n==1:
        print(a)
    elif n==2:
        print(a,b,end=" ")
        print()
    elif n==3:
        print(a,b,c,end=" ")
        print()
    else:
        print(a,b,c,end=" ")
        for i in range(3,n):
            a=b
            b=c
            c= a+b
            print(c,end=" ")
        print()

fibonacci(5)

fibonacci(10)
fibonacci(1)
fibonacci(2)
fibonacci(3)
fibonacci(4)
fibonacci(5)