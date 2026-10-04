print("write the factorial of a number")
def factorial(n):
    '''this function takes a number and return the factorial of this number'''
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))
'''this factorial function work polycy:-
1) n=5:- 5*factorial(4)
2) n=4:- 4*factorial(3)
3) n=3:- 3*factorial(2)
4) n=2:- 2*factorial(1)
5) n=1:- 1
'''