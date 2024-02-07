#Problem 1: Develop an application that asks the user for her/his name, and then greets them with their name.

def greet():
    person = input("Whats you name ?\n")
    return person

greetings = greet()
print("Hello", greetings)


