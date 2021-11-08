Name = "Michael Jackson"
Statement = Name + " is the best"
print(Name)
print(Statement)

print(Name[0])
print(Name[-1])

#Slicing
print(len(Name))
print(Name[0:4])
print(Name[8:12])

#Stride
print(Name[0:8:2])
print(Name[::2])

#Escape sequences : \ are meant to proceed escape sequences
print("Michael Jackson \nis the best")
print("Michael Jackson \tis the best")
print("Michael Jackson \\is the best")

#Methods
#upper() - lower()
A = "Thriller is the sixth studio album"
print(A.upper())
print(A.lower())

#replace()
print(Statement.replace('Michael','Janet'))

#find()
print(Name.find('a'))
print(Name.find('Jack'))

"""
Michael Jackson
Michael Jackson is the best
M
n
15
Mich
Jack
Mcal
McalJcsn
Michael Jackson 
is the best
Michael Jackson 	is the best
Michael Jackson \is the best
THRILLER IS THE SIXTH STUDIO ALBUM
thriller is the sixth studio album
Janet Jackson is the best
4
8


** Process exited - Return Code: 0 **
Press Enter to exit terminal
"""
