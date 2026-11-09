num=int(input("enter a number:"))
sum=0
while (num>0):
    digit=num%10
    sum=sum+digit
    num=num//10
print ("no of digit is=",sum)


list1=[1,2,3,4,2,6]
sum=0
for i in list1:
 sum= sum+i
print(sum)