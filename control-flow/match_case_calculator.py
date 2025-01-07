def calculator():
    
    # Prompt the user for two numbers
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    
    # Prompt the user fot the type operation they would want to perform
    operation = input("Choose the operation: (+, -, *, /): ")
    
    # Calculations using the match case
    match operation:
        
        # First case if operand is a plus sign perform Addition 
        case "+":
            print("The result is", num1 + num2)
        
        # If operation is - sign perform subtraction    
        case "-":
            print("The result is", num1 - num2)
            
        # If operation is a * asteric then perform multiplication
        case "*":
            print("The answer is", num1 * num2)
            
        # If operation is / then perform division
        case "/" if num2 != 0:
            print("The result is", num1 / num2)
            
        case "/":
            print("Cannot divide by zero")
            
        # Default if operation does not exist
        case _:
            print("This operation does not exist")
            
        
 
            
calculator()