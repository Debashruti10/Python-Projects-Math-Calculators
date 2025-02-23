def string_with_numbers(x):
    initial_value ="1"
    for i in range(2,x+1):
        initial_value=initial_value+"_"+str(i)
    return initial_value
print("string_with_numbers(3)->",string_with_numbers(3))
print("string_with_numbers(5)->",string_with_numbers(5))
