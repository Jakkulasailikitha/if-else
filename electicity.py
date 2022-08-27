a="  banana  , frisis, sikxsmxms"
print(a.strip())

amt=0
nu=int(input("enter the electricity unit"))
if nu<=100:
   amt=0
elif nu>100 and nu<=200:
   amt=(nu-100)*5
elif nu>200:
    amt=(nu-200)*10
print ("total amt:",amt)