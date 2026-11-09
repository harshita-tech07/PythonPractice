#wap a program to check the no is palindrom or not
num=int(input("enter the number:"))
x=num
rev=0
while num>0:
    digit=num%10
    rev=(rev*10)+digit
    num=num//10
if x==rev:
    print("number is palindrom")
else:
    print("number is not palindrom")


# s=input("enter a number:")
# if s==s[::-1]:
#  print("number is palindrom")
# else:
#  print("number is not palindrom")
