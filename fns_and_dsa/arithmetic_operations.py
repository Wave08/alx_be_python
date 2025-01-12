def perform_operation(num1, num2, operation):
    """This Function performs mathematical operation based on the user input and operation"""
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 == 0:
            raise ValueError("Cannot divide by zero")
        return num1 / num2
    else:
        raise ValueError(f"Invalid operation: {operation}")    
    
    
print(perform_operation(12, 0, "/"))
