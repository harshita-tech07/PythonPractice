for i in range(5):
 print()
 for j in range(5):
  print(i,end=" ")

for i in range(1,4):
 print ()
 for i in range(1,6):
  print(i,end=" ")



a, b = 0, 1
for i in range(10):
    print(a, end=" ")
    a, b = b, a + b

for i in range(1,6):
 print()
 for i in range(i+1):
  print(i,end=" ")


for i in range(6):
 print()
 for i in range(1,1+i):
  print("*", end=" ")
  print()


for i in range(7):
 print()
 for i in range(7,i,-1):
  print("*" , end=" ")

for i in range(1,6):
 print()
 for i in range(6-i):
  print(i, end=" ")