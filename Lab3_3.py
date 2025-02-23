


def closet_to_zero(num1,num2):
    num1_abs=abs(num1)
    num2_abs=abs(num2)
    if num1_abs<num2_abs:
        return num1
    return num2

def closest_to_zero_4(num1,num2,num3,num4):

    closest1 = closet_to_zero(num1, num2)
    closest2 = closet_to_zero(num3, num4)

    return closet_to_zero(closest1, closest2)

print(closest_to_zero_4(5,9,-2,11))
print(closest_to_zero_4(0,3,-2,4))
print(closest_to_zero_4(2,2,-2,1))