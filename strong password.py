"""
Q.1 Strong Password you have to create a strong password using nested if .
Conditions are :-A password is said to be strong if it satisfies the following criteria:
● It contains at least one lowercase English character.
● It contains at least one uppercase English character.
● It contains at least one special character. The special characters are: (@,#,$,%,&,_)
● Its length is at least 8.
● It contains at least one digit.(0 to 9)
Ex.1- input - Megha@8287
Output - Strong Password
Ex.2- Input - meghakashyap
Output - Not a strong Password
"""
print("welcome to the stong pass word world")
charcter1=input("enter the lower case character :")
CHARACTER2=input("enter the upper case  character : ")
special_character=input("enter the special character  :")
num=int(input("enter the number")) 
if charcter1>="a" and charcter1<="z":
	  if CHARACTER2>="A" and CHARACTER2<="Z":
                 if("special_character!=0"):  
                    if"num>0 and num<=9":
	                    print("good pass word")
else:
	  print("not pass word")