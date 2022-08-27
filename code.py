# i=int(input("enter the num1:"))
# j=int(input("enter the num2"))
# k=int(input("enter the num3:"))
# if i<j:
#     if j<k:
#         i=j
#     else:
#         j=k
# else:
#     if j>k:
#         j=i
#     else:
#         i=k
# print(i,j,k)

# a=["1","2","3","4"]
# # b=["apple","banana","orange","grapes"]
# e={}
# for x in range(len(a)-1):
#         d={a[x]:a[x+1]}
#         e.update(d)
# print(e)
a=[[5,6],[1,2],[5,9]]
i=0
sum=0
a=[]
while i<len(a):
        j=0
        while j<len(a[i]):
            sum+=a[i][j]
            j+=1
        a.append(sum)
        i+=1
print(sum)