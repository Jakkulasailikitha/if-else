#A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
# #Ask user for their salary and year of service and print the net bonus amount.
# # salary=float(input("enter the salary"))
# # service=float(input("enter the service of the employer"))
# # bonus=salary*0.05
# # if service>5:
# #     print("bonus amount",bonus,bonus+salary)
# # else:
# #     print("no bonus")


# n=int(input("enter the number:"))
# i=1
# while i<=n:
#     j=1
#     while j<=n-i:
#      print(" ",end=" ")
#      j=j+1
#     j=1
#     while j<=i:
#      print("*",end="   ")
#      j+=1
#     print()
#     i+=1
    
    
# n=int(input("enter the number:"))
# i=1
# while i<=n:
#     j=5
#     while j>=n-i:
#      print(" ",end=" ")
#      j=j-1
#     j=5
#     while j>=i:
#      print("*",end="   ")
#      j=j-1
#     print()
#     i+=1
    
    
# n=int(input("enter the number:"))
# for i in range (1,n):
#     for j in range(n,i,-1):
#         print(" ",end="")
#     for j in range(0,i):
#         print("*",end=" ")
#     print()
    
        
    
n=int(input("enter the number:"))
for i in range (1,n):
    for j in range(n,i,-1):
        print(" ",end="")
    for j in range(0,i):
        print("*",end=" ")
    print()