# """
# Q3. Your local library needs your help! Given the expected and actual return dates
# for a library book, create a program that calculates the fine (if any). The fee
# structure is as follows:
# 1.If the book is returned on or before the expected return date, no fine will
# be charged (i.e.: fine = 0).
# 2.If the book is returned after the expected return. but still within the samecalendar month and year as the expected return date, fine = Rs.15 * number of
# days late.
# 3.If the book is returned after the expected return month but still within the
# same calendar year as the expected return date, the fine = Rs.500 * number of
# days late.
# 4.If the book is returned after the calendar year in which it was expected,
# There is a fixed fine of Rs.10,000.
# """
# print("wel come to our library")
# print("there is a lot of books for you")
# print("please be slient when enter in to the library")

# expected_date=int(input("enter the expected date : "))
# expectedmonth=int(input('enter the expected month  :'))
# expected_year=int(input("enter the year :"))
# returndate=int(input("enter return date :"))
# returnmonth=int(input("enter the month"))
# return_year=int(input("enter the year"))
# if returndate<expected_date and returnmonth==expectedmonth and expected_year==return_year:
#     print("no fine for the students")
# if returndate>expected_date and returnmonth==expectedmonth and expected_year==return_year:
#     print((returndate-expected_date)*15)
# elif returndate>expected_date and returnmonth>expectedmonth and expected_year==return_year:
#     print(((returndate-expected_date)+(returnmonth-expectedmonth))*500)
# elif returndate<expected_date and returnmonth>expectedmonth and expected_year==return_year:
#     print(((returndate-expected_date)+(returnmonth-expectedmonth))*500)

# elif expected_year>return_year :
#     print("there is a fixed fine is 10000")     
    

    
# print("wel come to our library")
# print("there is a lot of books for you")
# print("please be slient when enter in to the library")

# expected_date=int(input("enter the expected date : "))
# expectedmonth=int(input('enter the expected month  :'))
# expected_year=int(input("enter the year :"))
# returndate=int(input("enter return date :"))
# returnmonth=int(input("enter the month"))
# return_year=int(input("enter the year"))
# if returndate<expected_date and returnmonth==expectedmonth and expected_year==return_year:
#     print("no fine for the students")
# if returndate>expected_date and returnmonth==expectedmonth and expected_year==return_year:
#     print((returndate-expected_date)*15)
# elif returndate>expected_date and returnmonth>expectedmonth and expected_year==return_year:
#     print(((returndate-expected_date)+(returnmonth-expectedmonth)*30)*500)
# elif expected_year>return_year :
#     print("there is a fixed fine is 10000") 
    
import random
numbers=[12,23,45,67,65,43]
random.shuffle(numbers)
print(numbers)