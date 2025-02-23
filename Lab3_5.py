def count(strings, target):
    
    occurrences = 0
    
    
    for string in strings:

        if string == target:
            occurrences =occurrences+1
    
    return occurrences


print(count(["a", "b", "c"], "b"))       
print(count(["a", "b", "c"], "e"))       
print(count(["a", "a", "a"], "a"))       