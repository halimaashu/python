import numbers
#
# def is_palindrome(word):
#     reverse_word=""
#     for ch in word:
#         reverse_word=ch+reverse_word
#     if reverse_word==word:
#         return True
#     else:
#         return False
# w=input("enter word")
# if is_palindrome(w):
#         print("palindrome")
# else:
#         print("not palindrome")
# def is_palindrome(word):
#     reverse_name=''
#     for ch in word:
#         reverse_name=ch+reverse_name
#     if reverse_name==word:
#         return True
#     else:
#         return False
# w=input('Enter a word: ')
# if is_palindrome(w):
#         print('Palindrome')
# else:
#         print('Not Palindrome')

# def odd_numbers(n):
#     events=[]
#     for n in n:
#         if n%2 !=0:
#             events.append(n)
#     return events
# numbers=[1,2,3,4,5,6,7,8,9]
# print("The Odd numbers are:",odd_numbers(numbers))


# def factorial_number(n):
#     if n == 0 or n == 1:
#         return 1
#     return n*factorial_number(n-1)
# n = int(input("Enter a positive number "))
# print(factorial_number(n))


# class Calculation:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

    # dighat shomikoron er pytohn program
import math
# class QuardraticEq:
#     def __init__(self, a, b,c):
#
#         d=(b*b)-(4*a*c)
#         if d<0:
#             print("Roots are imaginsry")
#         else:
#             x1=(-b+math.sqrt(d))/(2*a)
#             x2=(-b-math.sqrt(d))/(2*a)
#             print("X1=%2f"%x1,"X2=%2f"%x2)
#             print("Rots are real")
# a=int(input("Enter the number of A: "))
# b=int(input("Enter the number of B: "))
# c=int(input("Enter the number of C: "))
# qrdeq=QuardraticEq(a,b,c)





#using class calculate triangle area
# class TriangleArea:
#     def __init__(self,a,b,c):
#         if (a+b)>c and (a+c)>b and (b+c)>a:
#            s=(a+b+c)/2
#            area=math.sqrt(s*(s-a)*(s-b)*(s-c))
#            print("The triangle area is:",area)
#         else:
#             print("The triangle area is invalid")
# a=int(input("Enter the triangle value of A: "))
# b=int(input("Enter the  the triangle value of B: "))
# c=int(input("Enter the the triangle value of C: "))
# tarea=TriangleArea(a,b,c)


# using python find the largest number on three number

# class largeOne:
#     def __init__ (self,a,b,c):
#       if (a>b)and (a>c):
#           print("the large number is ",a)
#       elif(b>c):
#           print("the large number is ",b)
#       else:
#           print("the large number is ",c)
# a=int(input("enter the value of A="))
# b=int(input("enter the value of B="))
# c=int(input("enter the value of C="))
# lage=largeOne(a,b,c)

# class largeOne:
#     def __init__(self):
#         numbers=[12,12,13,78]
#         print(max(numbers))
#
# lage=largeOne()


#
# class ashik:
#  def __init__(self):
#      self.name="ashik mia"
#      self.age=18
#  def __str__(self):
#         return f"Name: {self.name}, Age: {self.age}"
#
# print(ashik())

# date time show in python
from  datetime import time
from  datetime import date
# from  datetime import datetime
# today=datetime.today()
# print ("todays Date and time: ",today)
# Make a function for multiply some number
# def multiply(number):
#     result=1
#     for i in number:
#         result= result*i
#     return result
# print("The result is",multiply((2,4,2)))

# def area():
#     try:
#         a=float(input("enter value of width: "))
#         b=float(input("enter value of lenght: "))
#         return a*b
#     except ValueError:
#         print("enter valid value")
#         return False
# result=area()
# if result!=False:
#     print("area is equal to ",result)
# else:
#     print ("try again laterf")
# def callculation(a,b):
#
#     add=a+b
#     sub=a-b
#     mul=a*b
#     div=a/b
#     return {"add":add, "sub":sub, "mul":mul, "div":div}
# print(callculation(10,5))














