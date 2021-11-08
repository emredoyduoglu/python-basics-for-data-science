#Lists are an ordered sequence
#Mutable
#Lists are written as comma-separated elements within square brackets

L = ["Michael Jackson", 10.1, 1982,"MJ",1]
print(L)
print(type(L))

#Mutable
L[0]="Janet Jackson"
print(L)

L[0]="Michael Jackson"
#Slicing
print(L[3:5])

#We can concatenate or combine lists by adding
L1 = L+ ["pop",10]
print(L1)

#extend()
L = ["Michael Jackson", 10.1, 1982]
print(L)
L.extend(["pop",10])
print(L)

#append()
L = ["Michael Jackson", 10.1, 1982]
print(L)
L.append(["pop",10])
print(L)

#String to list : split()
print("hard rock".split())
print("hard-rock".split('-'))

#Aliasing : Multiple names referring to the same object is known as aliasing.
A = ["hard rock",10,1.2]
B = A #both A and B are referencing the same list. 
B[0]="pop"
print(A)

#to clone list of A
C = A[:]
C[0] ="metal"
print(A)
print(B)
print(C)

"""
['Michael Jackson', 10.1, 1982, 'MJ', 1]
<class 'list'>
['Janet Jackson', 10.1, 1982, 'MJ', 1]
['MJ', 1]
['Michael Jackson', 10.1, 1982, 'MJ', 1, 'pop', 10]
['Michael Jackson', 10.1, 1982]
['Michael Jackson', 10.1, 1982, 'pop', 10]
['Michael Jackson', 10.1, 1982]
['Michael Jackson', 10.1, 1982, ['pop', 10]]
['hard', 'rock']
['hard', 'rock']
['pop', 10, 1.2]
['pop', 10, 1.2]
['pop', 10, 1.2]
['metal', 10, 1.2]


** Process exited - Return Code: 0 **
Press Enter to exit terminal
"""
