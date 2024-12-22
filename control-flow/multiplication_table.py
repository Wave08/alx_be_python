while True:
    try:
        number = int(input("Enter a number to see it's multiplication table: "))
    
        for num in range(1, 11):
            product = number * num
            print(f"{number} * {num} = ",product)
            
        another = input("Do you want to see another multiplication table: ").strip().lower()
        if another != "yes":
            print("Goodbye")
            break
        
    except ValueError as ve:
        print(ve)
        continue
    


