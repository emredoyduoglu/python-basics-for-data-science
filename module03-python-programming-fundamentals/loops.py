# Use the range

range(3)

# For loop example

dates = [1982,1980,1973]
N = len(dates)

for i in range(N):
    print(dates[i])     


# Example of for loop

for i in range(0, 8):
    print(i)

for i in range(0, 8,2):
    print(i)

# Exmaple of for loop, loop through list

for year in dates:  
    print(year)   


# Use for loop to change the elements in list

squares = ['red', 'yellow', 'green', 'purple', 'blue']

for i in range(0, 5):
    print("Before square ", i, 'is',  squares[i])
    squares[i] = 'white'
    print("After square ", i, 'is',  squares[i])


# Loop through the list and iterate on both index and element value

squares=['red', 'yellow', 'green', 'purple', 'blue']

for i , square in enumerate(squares):
    print(i, square)


# While Loop Example

dates = [1982, 1980, 1973, 2000]

i = 0
year = dates[0]

while(year != 1973):    
    print(year)
    i = i + 1
    year = dates[i]
    

print("It took ", i ,"repetitions to get out of loop.")


