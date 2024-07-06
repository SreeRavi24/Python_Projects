number=int(input("enter the marks  "))
if(number<35):
    print('fail')
elif(number==35):
    print('just pass')
elif(number==36 or number<=50):
    print('Average')
elif(number==51 or number<=80):
    print('above average')
elif(number==81 or number<=100):
    print('topper')
else:
    print('invalid marks')







