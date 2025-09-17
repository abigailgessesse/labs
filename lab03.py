# Part A ~ Temperature Conversion

def celsius_to_farenheit(celsius):
    farenheit = celsius * (9/5) + 32
    return farenheit

# Part B ~ Inches to Centimeters

def inches_to_centimeters(inches):
    centimeters = inches * 2.54
    return centimeters

#example
print(inches_to_centimeters(10))

# Part C ~ Total Bill
"""
# ASSUMING tip_percent will be sent as .20, if not, we would do tip_percent * .01
"""
def total_bill(meal_cost, tip_percent):
    tip_amount = tip_percent * meal_cost
    total_cost = meal_cost + tip_amount
    return total_cost

#example
print(total_bill(30, .15))