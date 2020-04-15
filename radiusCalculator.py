import math

# radius calculator

def radiusCalculator():

    user_radius = input("Please enter a radius: ")

    converted = int(user_radius)

    area = (math.pi) * (converted**2)

    print(area)

radiusCalculator()
