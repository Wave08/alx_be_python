# a simple function to add any two given numbers
def add(num1: int, num2: int) -> int:
    """This function simply adds two numbers"""
    num3 = num1 + num2
    return num3



num1, num2 = 10, 12 
ans = add(num1, num2)
print(f"The sum of {num1} and {num2} equals {ans}")


# Function to check is number is a prime number

def is_prime(n: int) -> int:
    # Check if the number is even and if its 1 then return False. 
    # 2 is the only even prime number
    if n in [2, 3]:
        return True
    if (n ==1) or (n % 2):
        return False
    
    # Loop to see if number n is divisible by an odd numbers up to it's square root
    r = 3
    while r * r <= n:
        if n % r == 0:
            return False
        r += 2
    return True
print(is_prime(9))


# Python Program to Illustrate 
# *args for variable number of arguments
def add(*argv):
    summ = 0
    for arg in argv:
        summ += arg
        
    print(summ)
        

add(34,34,10, 100, 190, 18000)


# Python program to illustrate 
# *kwargs for variable number of keyword arguments
def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))
        

# Driver code
myFun(first='Kudakwashe', mid='Jayden', last='flame')

