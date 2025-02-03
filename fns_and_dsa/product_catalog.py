products_catalog = []

def add_product(new_product):
    products_catalog.append(new_product)
    
def edit():
    options = input("Welcome to best shopping experience choose from these options: (remove, add, inset)")
    
    match options:
        case options == "add":
            products_catalog.__delitem__()
    