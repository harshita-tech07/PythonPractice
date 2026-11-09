l={1:10,2:30,3:30}
l.pop(2)
print(l)

d={'name':'harshita','age':20,'city':'pune'}
print (d['name'])
#wap to create a user defined dictonary
d={}
n=int(input("enter how many items you want to enter in dictionary:"))
for i in range(n):
    key=input("enter the key:")
    item=input("enter the  item:")
    d [key]=item
print(d)

#wap to create dictonary in the format
{1:1,2:4,3:9,4:16}
d={}
n=int(input("how many item you want to enter:"))
for i in range(n):
    key=i+1
    value =key**2
    d[key]=value
print(d)
print("hello world")


