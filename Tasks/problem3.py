#Problem 3: You have been asked to create an application for the Student Union shop which sells caps for 5, shirts for 10 and hoodies for 20. Your application should allow the user to input the quantity of each item a student wants to buy and then calculate and output the total cost. When you have finished the implementation, test your application to ensure that the calculations are correct.


def items():

    caps = int(input("Please enter caps you would like to buy ?\n"))
    shirts = int(input("Please enter shirts you would like to buy ?\n"))
    hoodies = int(input("Please enter hoodies you would like to buy ?\n"))

    caps_cost = caps * 5
    shirts_cost = shirts * 10
    hoodies_cost = hoodies * 20

    total_cost = caps_cost + shirts_cost + hoodies_cost

    return total_cost

print(items())



