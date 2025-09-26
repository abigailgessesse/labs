# PART A
# The random module is what let's us make calls to get random integers
import random

# This function simulates flipping a coin. It returns the string H for heads
# and T for tails
def flip_coin():
    coin = ''
    flip = random.randint(1, 10)
    if flip <= 5:
      coin = 'H'
    else:
      coin = 'T'
    return coin

# This function simulates taking a number of steps. It will return an integer
# number of steps to take
def get_steps():
    steps = random.randint(1, 50)
    return steps

# Use this variable to keep track of your position
position = 50
left_wall = 0
right_wall = 100
"""
for i in range(5):
   coin = flip_coin()
   steps = get_steps()
   if coin == 'H':
      position += steps
   else:
      position -= steps
   if position <= left_wall or position >= right_wall:
    print('You win!')
   else:
    print('You are at position', position, 'in the room.')
"""
# PART B
# Reset your position to the center of the room
position = 50

# Set your counter to see how many chances you have taken to reach the wall
counter = 0

# TODO: While you haven't reached the left wall or right wall:
while left_wall < position < right_wall:
    # Get a random number of steps
    steps = get_steps()
    # Flip a coin
    coin1 = flip_coin()
    # Flip another coin
    coin2 = flip_coin()
    # Debug print steps and coin flips
    # print out steps, coin1, and coin2
    # print("steps: " + str(steps) + "1st coin: " + str(coin1) + " 2nd coin: " + str(coin2))
    # If the first coin toss is the same as the second:
        # Double the number of steps
    if coin1 == coin2:
       steps *= 2
    if coin1 == "H":
       position += steps
    else: position -= steps
    # Increment your counter for each iteration
    counter += 1    


# The following statement does not need to be changed.
print('You reached the wall after', counter, 'chances.')

# The code below is for us to test your code. Do not modify it.
assert(counter > 0)
assert(position <= left_wall or position >= right_wall)