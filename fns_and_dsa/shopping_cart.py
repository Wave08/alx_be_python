# Shopping Cart Program
foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q":
        print("Thanks For Shopping!")
        break
    else:
        price = float(input(f"Enter the prize of a {food}: $"))
        foods.append(food)
        prices.append(price)
    
print("----- YOUR CART -----")

for food in foods:
    print(food, end=" ")
    
for price in prices:
    total += price
    
    
print(f"\nThe total price for your cart is: ${total}")