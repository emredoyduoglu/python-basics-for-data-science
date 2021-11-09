# potential code before try catch

a = 1

try:
    # code to try to execute
    b = int(input("Please enter a number to divide a"))
    a = a/b
    print("Success a=",a)
except:
    # code to execute if there is an exception
    print("There was an error")

# code that will still execute if there is an exception

# try except specific example

a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
    print("Success a=",a)
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")


a = 1

#try except else

try:
    # code to try to execute
    b = int(input("Please enter a number to divide a"))
    a = a/b
except ZeroDivisionError:
    # code to execute if there is a ZeroDivisionError
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    # code to execute if there is a ValueError
    print("You did not provide a number")
except:
    # code to execute if ther is any exception
    print("Something went wrong")
else:
    # code to execute if there is no exception
    print("success a=",a)
finally:
    # code to execute at the end of the try except no matter what
    print("Processing Complete")

# code that will execute if there is no exception or a one that we are handling



