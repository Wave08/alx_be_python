while True:
    try:
        num1 = int(input("\nEnter the first number: "))
        num2 = int(input("Enter the second number: "))
    except ValueError as ve:
        print("Error: ",ve)
        continue
    

    
    operator = (input("\nChoose the operation (+, -, *, /): "))


    if operator == "+":
        result = num1 + num2
        print("The result is",result)
    elif operator == "-":
        result = num1 - num2
        print("The result is",result)
    elif operator == "*":
        result = num1 * num2
        print("The result is",result)
    elif operator == "/":
        try:
            result = num1 / num2
            print("The result is ", result)
        except ZeroDivisionError as zd:
            print("Error:", zd)
            continue
    else:
        print("That is an invalid operator")
        continue
    
    # Prompt if the user still wants to perform another calculation
    another = input("Do you want to perform another calculation: ").strip().lower()
    
    if another != "yes":
        print("Goodbye")
        break


    