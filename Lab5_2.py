import xml.etree.ElementTree as ET

memory = 0
operation = ""
first_operand = int(input("Enter initial number: "))
memory_list = [first_operand]
memory = first_operand

while True:
    operation = input("Enter operation (load/store/add/sub/mul/undo/div/quit): ")
   
    if operation == "quit":
        print("The program quit with a memory of " + str(memory))
        break
   
    if operation == "undo":
        if len(memory_list) <= 1:
            print("There is nothing to undo.")
        else:
            memory_list.pop()
            memory = memory_list[-1]
   
    elif operation == "store":
        numbers = ET.Element("numbers")
        for value in memory_list:
            number = ET.SubElement(numbers, "number")
            number.text = str(value)

        xml_string = ET.tostring(numbers, encoding="unicode")
        with open("memory.xml", "w") as xml_file:
            xml_file.write(xml_string)
        print("State stored successfully.")

    elif operation == "load":
        try:
            with open("memory.xml", "r") as xml_file:
                xml_string = xml_file.read()
            numbers_element = ET.fromstring(xml_string)
           
            memory_list = [int(number.text) for number in numbers_element]
            memory = memory_list[-1]
            print("State loaded successfully.")
        except FileNotFoundError:
            print("No stored state found.")
        except ET.ParseError:
            print("Error parsing the stored state.")
        except Exception as e:
            print(f"An error occurred: {e}")
   
    else:
        operand = int(input("Enter operand: "))

        if operation == "add":
            memory += operand
            memory_list.append(memory)

        elif operation == "sub":
            memory -= operand
            memory_list.append(memory)

        elif operation == "mul":
            memory *= operand
            memory_list.append(memory)

        elif operation == "div":
            if operand == 0:
                print("Cannot divide by zero.")
            else:
                memory /= operand
                memory_list.append(memory)

        else:
            print("Invalid operation. Please try again.")
   
    if operation not in ["quit", "store", "load"]:
        print(str(memory_list[-1]) + " is stored in memory")
        print(memory_list)

