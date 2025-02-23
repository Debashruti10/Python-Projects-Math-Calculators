imp1=int(input("enter the first number: "))
imp2=int(input("enter the second number: "))
def closet_to_zero(num1,num2):
    num1_abs=abs(num1)
    num2_abs=abs(num2)
    if num1_abs<num2_abs:
        return num1
    return num2
print("closest_to zero(",imp1,",",imp2,")->",closet_to_zero(imp1,imp2))

        

    