#Tuples are an ordered sequence
#Immutable
#Tuples are written as comma-separated elements within parentheses

Ratings = (10,9,6,5,10,8,9,6,2)
print(Ratings)
print(type(Ratings))

tuple1 = ('disco',10,1.2)
print(type(tuple1))

print(tuple1[0])
print(tuple1[-1])

tuple2 = tuple1 + ("hard rock", 10)
print(tuple2)

#Slicing
print(tuple2[0:3])

#Lenght
print(len(tuple2))

#sorted : return list
print(sorted(Ratings))

#Nested tuples
NT = (1,2,("pop","rock"),(3,4),("disco",(1,2)))
print(NT[2])
print(NT[2][0])
print(NT[2][1])
print(NT[4][1])
print(NT[4][1][0])

"""
(10, 9, 6, 5, 10, 8, 9, 6, 2)
<class 'tuple'>
<class 'tuple'>
disco
1.2
('disco', 10, 1.2, 'hard rock', 10)
('disco', 10, 1.2)
5
[2, 5, 6, 6, 8, 9, 9, 10, 10]
('pop', 'rock')
pop
rock
(1, 2)
1


** Process exited - Return Code: 0 **
Press Enter to exit terminal
"""
