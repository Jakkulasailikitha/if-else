"""
A student will not be allowed to sit in exam if his/her attendence is less than 75%.
Take following input from user
Number of classes held
Number of classes attended.
And print
percentage of class attended
Is student is allowed to sit in exam or not.
"""
#classes=int(input("enter that how many classes they held in class"))
#classes=int(input("the number of classes that he/she attended"))
#percentage=float(input("enter the percentage"))
#if percentage>0.75:
   # print("you are allowed for the exam")
#else:
    #print("you are allowed for the exam")
 # to find the second maximum
num1=int(input("enter the number")) 
num2=int(input("enter the number"))
num3=int(input("enter the number")) 
if num1>num2 and num1>num3:
   if num3>num2 and num3>num1:
       print(num3,"num3 is maximu" )
   else:
        print(num1,"num1 is maximum",)
else:
    if num2<num3 and num2>num1:
        print(num2,"num2 is maximum")