print("i am writing a function for fibonacci series")


def fibonacci(n):
    #  F(n) = F(n-1) + F(n-2)
    '''this is fibonacci function which is the best option'''
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # print(fibonacci(n - 1) + fibonacci(n - 2))
        return fibonacci(n - 1) + fibonacci(n - 2)

n=int(input("enter the fibonacci no n="))
print(fibonacci(n))

