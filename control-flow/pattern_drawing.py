try:
    # Initialize the rows counter
    row = 0
    # Prompt the user to enter the size of the pattern
    size = int(input("Enter the size of the pattern: "))
    # Utilize the while loop to control the number of rows based on the size thus to draw the pattern
    while row < size:
        for col in range(size):
            print("*", end="")
    
        # Move to the next line after each row
        print()
        # Increment row counter    
        row+=1
except ValueError as ve:
    print(ve)



    
    
    