# Read the Example1.txt

example1 = "data/example1.txt"
file1 = open(example1, "r")

# Print the path of file

file1.name

# Print the mode of file, either 'r' or 'w'

file1.mode

# Read the file

FileContent = file1.read()
FileContent

# Print the file with '\n' as a new line

print(FileContent)

# Type of file content

type(FileContent)

# Close file after finish

file1.close()

# Open file using with

with open(example1, "r") as file1:
    FileContent = file1.read()
    print(FileContent)
    
# Read first four characters

with open(example1, "r") as file1:
    print(file1.read(4))
    
# Read certain amount of characters

with open(example1, "r") as file1:
    print(file1.read(4))
    print(file1.read(4))
    print(file1.read(7))
    print(file1.read(15))
    
# Read one line

with open(example1, "r") as file1:
    print("first line: " + file1.readline())

with open(example1, "r") as file1:
    print(file1.readline(20)) # does not read past the end of line
    print(file1.read(20)) # Returns the next 20 chars
    
# Iterate through the lines

with open(example1,"r") as file1:
        i = 0;
        for line in file1:
            print("Iteration", str(i), ": ", line)
            i = i + 1
            
# Read all lines and save as a list

with open(example1, "r") as file1:
    FileasList = file1.readlines()
    
# Print the first line

FileasList[0]

# Print the third line

FileasList[2]
