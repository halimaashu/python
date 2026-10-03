# function and arguments
# def average(a,b):
#     print("The average of",a,"and",b,"is",(a+b)/2)
# average(10,20)
def average(*numbers):
   
    sum=0
    for i in numbers:
        sum+=i
    print ("The average of",numbers,"is=",sum/len(numbers))  


average(1,2,3,4,5,6,7,8)