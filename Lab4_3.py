def sums(numbers):
    
    result = {"odd": 0, "even": 0, "all": 0}
    
    
    for num in numbers:
        result["all"] += num  
        if num % 2 == 0: 
            result["even"] += num
        else: 
            result["odd"] += num
    
    
    return result
print("sums((1,2,3,4,5)): ",sums((1,2,3,4,5)))
print("sums((2,4,6)): ",sums((2,4,6)))
