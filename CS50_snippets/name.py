import os
import sys
#sys.arg system argument to provide before entering elements

if len(sys.argv) < 2:
    sys.exit("Too few arguments")


for arg in sys.argv[1:-1]: #negative number goes from right to left and remove the right arguments
    print("Hello, name is ", arg)




# if len(sys.argv) < 2:
#     sys.exit("Too few Args") #this will termninate the program if the input is not correct
# elif len(sys.argv) < 2:
#     sys.exit("Too many Arg")

# print("Hello my name is ", sys.argv[1])



# if len(sys.argv) < 2:
#     print("Too few argument")
# elif len(sys.argv) > 2:
#     print("Too many Argument")
# else:
#     print("Hello, name is", sys.argv[1])

# try:
#     print("Hello, name is", sys.argv[1], sys.argv[2])
# except IndexError:
#     print("Please add two parameters ")


