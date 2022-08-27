n=int(input("enter the number"))
m=n
s=0
while n>0:
    r=n%10
    s=s+r*r*r
    n=n//10
if s==m:
    print("given number is armstrong",m)
elif n**1==n:
    print("armstrong")
else:
   print("given number is  not armstrong",)