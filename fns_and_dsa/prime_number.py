def is_prime_num(num):
    """A Function finds and prints all prime numbers 
       with a specified range in this case from 0 to 100
    """
    
    
   
    if num == 2:
       return True
    if num == 1:
       return False
       
    div = 3
    while div < num:
       
       if (div * div) % num == 0:
          return False
          div += 2
       return True
       
       
print(is_prime_num(10))