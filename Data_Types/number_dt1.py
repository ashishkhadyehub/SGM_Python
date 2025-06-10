import math
import random

print("Floor of 45.56:", math.floor(45.56))          # 45
print("Floor of -3.5:", math.floor(-3.5))            # -4

print("Truncate -2.8:", math.trunc(-2.8))            # -2 (drops decimal, towards 0)
print("Ceiling of 45.56:", math.ceil(45.56))         # 46

print("Factorial of 5:", math.factorial(5))          # 120
print("Square root of 16:", math.sqrt(16))           # 4.0

print("Power 2^5:", math.pow(2, 5))                   # 32.0

print("Value of PI:", math.pi)                        # 3.141592...

print("Round of 34.56:", round(34.56))                # 35
print("Round of 34.56789 to 2 decimal places:", round(34.56789, 2))  # 34.57

print(random.randint(90,100))
l1=[11,22,33,44,55,66,77]  
print(random.choice(l1)) 
random.shuffle(l1)
print(l1)