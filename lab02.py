# Part A - Intro
name = input("What is your name? ")

summer = 0
fall = 0
winter = 0
spring = 0

# Part B - Questions

# Question #1
print("What color do you like the most?")
print(" 1) Red") #summer
print(" 2) Blue") #fall
print(" 3) Green") #winter
print(" 4) Yellow") #spring
color = input("Enter the number of your choice: ")

if color == "1":
    summer += 1
elif color == "2":
    fall += 1
elif color == "3":
    winter += 1
elif color == "4":
    spring += 1

# Question #2
print("Do you like warm or cold?")
print(" 1) Warm") #summer and spring
print(" 2) Cold") #fall and winter
weather = input("Enter the number of your choice: ")
if weather == "1":
    summer += 1
    spring += 1
if weather == "2":
    fall += 1
    winter += 1

# Question #3
print("Do you like drinking warm drinks or cold drinks?")
print("1) Warm Drinks") 
print("2) Cold Drinks")
drink_choice = input("Enter the number of your choice: ")
if drink_choice == "1":
    print("Do you like hot cocoa or tea?")
    print("1) Hot cocoa") #winter
    print("2) Tea") #spring
    hot_second_choice = input("Enter the number of your choice: ")
    if hot_second_choice == "1":
        winter += 1
    elif hot_second_choice == "2":
        spring += 1

if drink_choice == "2":
    print("Do you like lemonade or iced tea?")
    print("1) Lemonade") #summer
    print("2) Iced tea") #fall
    cold_second_choice = input("Enter the number of your choice: ")
    if cold_second_choice == "1":
        summer += 1
    elif cold_second_choice == "2":
        fall += 1

# Question #4
print("What activity do you like to do outside?")
print("1) Swimming") #summer
print("2) Skiing") #winter
print("3) Garden") #spring
print("4) Hike") #fall
activity = input("Enter the number of your choice: ")

if activity == "1":
    summer += 1
elif activity == "2":
    winter += 1
elif activity == "3":
    spring += 1
elif activity == "4":
    fall += 1


# Question #5
"""
had to use different approach for months, as if month = "_" or "_" would falsely evaluate
statements as true, giving wrong scores
"""
month = input("What month were you born in? ")    
if month in ("June", "July", "August"):
    summer += 1
elif month in ("September", "October", "November"):
    fall += 1
elif month in ("December", "January", "February"):
    winter += 1
elif month in ("March", "April", "May"):
    spring += 1

# Part C - Results


# How can you find the season with the max count?
"""
I did this by starting with a season to compare to each season at the end, in a king of the hill way
Once a season is higher than Fall, it'll become the new season and new max score, and continue as
such for the rest of the seasons. As for the alphabetical aspect, in case of a tie, I said if the
score is equal AND the string of the season holds a lower Unicode points (ty Google), then it will
update as the new max score. 
"""

season = 'Fall'

max_score = fall

if (summer > max_score) or (summer == max_score and "Summer" < season):
    season = 'Summer'
    max_score = summer

if (spring > max_score) or (spring == max_score and "Spring" < season):
    season = 'Spring'
    max_score = spring

if (winter > max_score) or (winter == max_score and "Winter" < season):
    season = 'Winter'
    max_score = winter


#The following code does not need to be changed

print("Thank you for taking the quiz", name, "!")
print("You are most like", season)
print(spring)
print(summer)
print(fall)
print(winter)