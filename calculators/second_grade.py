import math

# equation bring by the way ax + bx + c = 0
def second_grade_equation(a, b, c):
    discriminator = (math.pow(b, 2) - 4 * a * c)
    if discriminator < 0:
        print("there's no real solution for that discriminator.")
    else:
        x = (-b + math.sqrt(discriminator)) / 2 * a
        print(f"the value of x is: {x}")
