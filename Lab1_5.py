number=int(input("put number"))
number1=int(input("put lower boundary"))
number2=int(input("put upper boundary"))
for i in range(number1, number2+1):
    print( str(i)+ "*" +str(number)+ "="+ str(i*number))

