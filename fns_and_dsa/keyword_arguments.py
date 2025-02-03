# This Python Script demonstrates the use of keyword arguments and returns their values in formatted string

def cheeseshop(**kwargs):
    for key, value in kwargs.items():
        print("You bought %s %s %s each" % key[0], key[1], key[2])
    
    

    
    
    
shop = cheeseshop(item="sweets", quantity="5", price="1.50")