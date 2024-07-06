sum=0
count=0
a=int(input("Enter number1 "))
b=int(input("Enter number2 "))
for i in range(a,b):
    print(i)
    sum=sum+i
    count=count+1
    average=sum/count
print("sum of numbers",sum)
print("count of the numbers",count)
print("average of the numbers",average)


