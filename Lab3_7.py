


memory = int(input("Enter initial memory value: "))


while True:

    operation = input("Enter operation (add/sub/mul/div/quit): ")
    
    if operation == "quit":
        print("The program finished with", memory, "stored in memory.")
        break  


    operand = int(input("Enter operand: "))

    
    if operation == "add":
        memory += operand  
    elif operation == "sub":
        memory -= operand  
    elif operation == "mul":
        memory *= operand  
    elif operation == "div":
        if operand != 0: 
            memory/=operand 
        else:
            print("Error: Division by zero is not allowed.")
            continue  
        
    else:
    
        print("Invalid operation. Please enter add, sub, mul, div, or quit.")

    print(memory, "is stored in memory.")
