firstName="John"
lastName="Doe"
fullName=f"{firstName} {lastName}"
print(f"i am using the -f string write this {{fullName}} the name is ={fullName}")


def square(n):
    '''this function takes a number and make 
    this square of the number'''
    print(f"The square of {n} is {n**2}")
square(6)
print(square.__doc__)