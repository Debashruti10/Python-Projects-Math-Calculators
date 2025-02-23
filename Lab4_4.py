
memory = int(input("Enter initial memory value: "))
value=[memory]

while True:

    operation = input("Enter operation (add/sub/mul/div/quit/undo): ")
    
    if operation == "quit":
        print("The program finished with",{memory},"in memory.")
        break  
    elif operation == "undo":
        if len(value)>1:
            value.pop()
            memory=value[-1]
            print({memory},"is stored in memory.")
        else:
                print("there is nothing to undo")
    
    elif operation in ["add", "sub", "mul", "div"]:
        try: 
            operand = int(input("Enter operand: "))
              
            if operation == "add":
                memory = memory + operand
            elif operation == "sub":
                memory = memory - operand
            elif operation == "mul":
                memory = memory * operand
            elif operation == "div":
                if operand == 0:
                    print("Error: Division by zero is not allowed.")
                    continue
                memory = memory // operand  
            
            value.append(memory)  
            print(f"{memory} is stored in memory.")
        except ValueError:
            print("Invalid operation. Please try again.")
    else:
        print("Invalid operation.Please try again")
    
  