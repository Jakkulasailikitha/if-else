quantity=int(input("enter the quantity"))
cost=quantity*100
if cost>1000:
   discount=0.1*quantity
   amount_paid =cost-discount
   print("discount amount",discount)
   print("total amount",amount_paid)
else:
   print(" noo  discount amount ")