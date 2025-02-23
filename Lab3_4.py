def highest(numbers):

    highest_value=numbers[0]

    for num in numbers:
        if num>highest_value:
            highest_value=num
    return highest_value
print(highest([5,3]))
print(highest([2,8,4,3]))
print(highest([-2,-5]))
print(highest([42]))