def are_equal(list1, list2):
  
    if len(list1) != len(list2):
        return False
    
 
    for i in range(len(list1)): 
        if list1[i] != list2[i]:  
            return False
    
    
    return True
print("are_equal((1,2,3),(1,2,3)): ", are_equal((1,2,3),(1,2,3)))
print("are_equal((1,2,3),(1,2,2)): ", are_equal((1,2,3),(1,2,2)))
print("are_equal((1,2,3),(1,2)): ", are_equal((1,2,3),(1,2)))