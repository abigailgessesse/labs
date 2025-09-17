# Part A

name = input("What is your name? ")

meal = input(name + ", what would you like to eat? ")
drink = input(name + ", what would you like to drink? ")

print("Thank you, " + name + ". You ordered a " + drink + " and a " + meal + ".")

# Part B

"""
IMPORTANT: assuming tip is off the bill BEFORE tax
if AFTER tax, it'll be tip_amount = .20 * (bill + sales_tax)
"""

bill = 148.45
tip_amount = .20 * bill
sales_tax = bill * .10
total = bill + tip_amount + sales_tax
cost_each = total / 6
print (cost_each)