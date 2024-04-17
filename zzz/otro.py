import random
import math
e = math.e
d = 3
m = 6
while True:
    r = random.random()
    r2 = random.random()
    x_1 = math.sqrt(-2 * math.log(1-r, e)) * math.cos(2 * math.pi * r2) * d + m
    if r == 1:
        print("se complico")
        
        break