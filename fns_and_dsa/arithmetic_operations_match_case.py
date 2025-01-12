def perform_operations():
    """A function that performs basisc arithmetic operations based on user input"""
    
    # Ask for user input
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    
    # Ask the user for type of operation 
    operation = input("Choose the operation: (+, -, / *)")
    
    # Use match case to perform different operations based on the user choice
    match operation:
        
        case "+":
            ans = num1 + num2
            print(f"{num1} {operation} {num2} = {ans}")
        
        case "-":
            ans = num1 - num2
            print(f"{num1} {operation} {num2} = {ans}")
            
        case "/":
            if num2 == 0:
                raise TypeError("Cannot divide by zero")
            ans = num1 / num2
            print(f"{num1} {operation} {num2} = {ans}")
            
        case "*":
            ans = num1 * num2
            print(f"{num1} {operation} {num2} = {ans}")
            
        case _:
            print("Operation does not exist")
            
            
    
perform_operations()