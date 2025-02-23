def change_to_highest(the_list):
   
    for i in range(len(the_list)):
       
        the_list[i] = max(the_list[i])  
the_list=[    
    [1, 2, 3],
    [5, 4, 3],
    [2, 7, 6]
]
change_to_highest(the_list)
print((the_list))