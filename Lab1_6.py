
product=1
number=int(input("enter the lower number of the range"))
number1=int(input("enter the upper number of the range"))
for i in range(number, number1+1):
    product=product*i
print("the product of the integer between 3 and 5 is"+ str(product))

