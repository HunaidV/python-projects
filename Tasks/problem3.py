#Problem 3: You have been asked to create an application for the Student Union shop which sells caps for 5, shirts for 10 and hoodies for 20. Your application should allow the user to input the quantity of each item a student wants to buy and then calculate and output the total cost. When you have finished the implementation, test your application to ensure that the calculations are correct.


caps = int(input("Please enter caps you would like to buy ?\n"))
# shirts = int(input("Please enter shirts you would like to buy ?\n"))
# hoodies = int(input("Please enter hoodies you would like to buy ?\n"))


def cost(c):
    d = 1
    for n in range(d, c):
        return n * 5

print(cost(caps))