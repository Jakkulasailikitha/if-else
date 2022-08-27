#A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
#Ask user for their salary and year of service and print the net bonus amount.
salary=float(input("enter the salary"))
service=float(input("enter the service of the employer"))
bonus=salary*0.05
if service>5:
    print("bonus amount",bonus,bonus+salary)
else:
    print("no bonus")