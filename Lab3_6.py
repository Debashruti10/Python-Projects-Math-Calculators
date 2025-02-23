
num1 = int(input("Enter the first (lower) integer: "))
num2 = int(input("Enter the second (higher) integer: "))


if num1 >= num2:
    print("The first integer should be lower than the second integer.")
else:

    even_sum = 0
    
    
    for i in range(num1, num2 + 1):
        
        if i % 2 == 0:
           
            even_sum=even_sum+i
    
   
    print("The sum of even integers between", num1, "and", num2, "is:", even_sum)