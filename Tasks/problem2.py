#Problem 2: Write an application that displays the recommended weight given the user’s age and height (in centimeters) using the following formula: RW = (height -100 + age % 10) * 0.90

user_age = int(input("What is your age?\n"))
user_height = int(input("Whats your height?\n"))

def bmi(a, b):
    RW = (a - 100 + b % 10) * 0.90
    return RW * -1


recommened_weight = bmi(user_age, user_height)
print(recommened_weight)