number = int(input("What's number: "));

def fib(n):    
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

fib(number)
