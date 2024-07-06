a=int(input('enter the first number  '))
b=int(input('enter the second number '))
c=input('do you want add or sub or multiply or divide')
d= a+b
e= a-b
f=a*b
g=a/b
if(c=="add"):
    print(d)
elif(c=="sub"):
    print(e)
elif(c=="multiply"):
     print(f)
elif(c=="divide"):
     print(g)
else:
    print("get lost")
