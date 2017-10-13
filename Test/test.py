# This is a simple program that takes input from the command line and prints the arguments

# Import allow us to use functions and variables from pre-written packages
# The format is: import package-name
import sys

# We can pass information to a program when it runs; this allows us to pass information to the script at runtime
# We check the number of command line arguments with the variable:
num_args=len(sys.argv)

# Here we declares an empty list that we can add to later
# A list is different from an array in the sense it can grow; array size is fixed
arg_storage=[]

# Now that we have declared some variables we make a function to check what args the script received
def argHandler():
    
    # Checks if no arguments were passed
    # We check num_args == 1 because when we execute a script the first parameter is the file name
    # ie) sys.argv[0] == test.py; from the command line 'python test.py'
    if (num_args == 1):
        print("No arguments passed")
    
    # This section executes if the first statement fails
    else:
        # Here we iterate over the arguments passed and add them to our list: arg_storage
        # We already stored the number of arguments, so we have our bound for looping
        for x in range(num_args):
            arg_storage.append(sys.argv[x])

# Here we are calling the function we declared earlier
# Notice the empty brackets; if the function had parameters we must match the function prototype declared
argHandler()

# Once we have built our list we print the contents, to do this we will make another function to print it
# Notice the function takes a parameter this time; in this case a list
def argPrinter(temp_list = []):

    # Loops over the list we defined earlier: arg_storage
    for x in range(len(temp_list)):
        print(temp_list[x])

# Now we want to call our print function and print the list contents
# When we call our function we need to pass our list as the parameter
argPrinter(arg_storage)
