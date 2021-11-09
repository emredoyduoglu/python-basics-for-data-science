# First function example: Add 1 to a and store as b

def add(a):
    """
    help message : add 1 to a
    """
    b = a + 1
    print(a, "if you add one", b)
    return(b)
help(add)

add(1)

# Define a function for multiple two numbers

def Mult(a, b):
    c = a * b
    return(c)
    print('This is not printed')
    
result = Mult(12,2)
print(result)


# Function Definition
def square(a):
    
    # Local variable b
    b = 1
    c = a * a + b
    print(a, "if you square + 1", c) 
    return(c)
# Initializes Global variable  

x = 3
# Makes function call and return function a y
y = square(x)
print(y)

# Define functions, one with return value None and other without return value

def MJ():
    print('Michael Jackson')
    
def MJ1():
    print('Michael Jackson')
    return(None)

MJ()
MJ1()
# See what functions returns are

print(MJ())
print(MJ1())

# Define the function for combining strings

def con(a, b):
    return(a + b)
# Test on the con() function

print(con("This ", "is"))


# Function example

def type_of_album(artist, album, year_released):
    
    print(artist, album, year_released)
    if year_released > 1980:
        return "Modern"
    else:
        return "Oldie"
    
x = type_of_album("Michael Jackson", "Thriller", 1980)
print(x)

# Print the list using for loop

def PrintList(the_list):
    for element in the_list:
        print(element)
PrintList(['1', 1, 'the man', "abc"])

# Example for setting param with default value

def isGoodRating(rating=4): 
    if(rating < 7):
        print("this album sucks it's rating is",rating)
        
    else:
        print("this album is good its rating is",rating)

isGoodRating()
isGoodRating(10)

# Example of global variable

artist = "Michael Jackson"
def printer1(artist):
    internal_var1 = artist
    print(artist, "is an artist")
    
printer1(artist)
# try runningthe following code
#printer1(internal_var1) 

artist = "Michael Jackson"

def printer(artist):
    global internal_var 
    internal_var= "Whitney Houston"
    print(artist,"is an artist")

printer(artist) 
print(internal_var)
printer(internal_var)


# Example of global variable

myFavouriteBand = "AC/DC"

def getBandRating(bandname):
    if bandname == myFavouriteBand:
        return 10.0
    else:
        return 0.0

print("AC/DC's rating is:", getBandRating("AC/DC"))
print("Deep Purple's rating is:",getBandRating("Deep Purple"))
print("My favourite band is:", myFavouriteBand)

# Deleting the variable "myFavouriteBand" from the previous example to demonstrate an example of a local variable 

del myFavouriteBand

# Example of local variable

def getBandRating(bandname):
    myFavouriteBand = "AC/DC"
    if bandname == myFavouriteBand:
        return 10.0
    else:
        return 0.0

print("AC/DC's rating is: ", getBandRating("AC/DC"))
print("Deep Purple's rating is: ", getBandRating("Deep Purple"))
#print("My favourite band is", myFavouriteBand)


# Example of global variable and local variable with the same name

myFavouriteBand = "AC/DC"

def getBandRating(bandname):
    myFavouriteBand = "Deep Purple"
    if bandname == myFavouriteBand:
        return 10.0
    else:
        return 0.0

print("AC/DC's rating is:",getBandRating("AC/DC"))
print("Deep Purple's rating is: ",getBandRating("Deep Purple"))
print("My favourite band is:",myFavouriteBand)

#Collections and Functions

def printAll(*args): # All the arguments are 'packed' into args which can be treated like a tuple
    print("No of arguments:", len(args)) 
    for argument in args:
        print(argument)
#printAll with 3 arguments
printAll('Horsefeather','Adonis','Bone')
#printAll with 4 arguments
printAll('Sidecar','Long Island','Mudslide','Carriage')


def printDictionary(**args):
    for key in args:
        print(key + " : " + args[key])

printDictionary(Country='Canada',Province='Ontario',City='Toronto')



def addItems(list):
    list.append("Three")
    list.append("Four")

myList = ["One","Two"]

addItems(myList)

print(myList)