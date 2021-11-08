# Create the dictionary
Dict = {"key1": 1, "key2": "2", "key3": [3, 3, 3], "key4": (4, 4, 4), ('key5'): 5, (0, 1): 6}
print(Dict)

# Access to the value by the key
print(Dict["key1"])

# Access to the value by the key
print(Dict[(0, 1)])

# Create a sample dictionary
release_year_dict = {"Thriller": "1982", "Back in Black": "1980", \
                    "The Dark Side of the Moon": "1973", "The Bodyguard": "1992", \
                    "Bat Out of Hell": "1977", "Their Greatest Hits (1971-1975)": "1976", \
                    "Saturday Night Fever": "1977", "Rumours": "1977"}
                    
print(release_year_dict)

# Get value by keys
print(release_year_dict['Thriller'])

# Get all the keys in dictionary
print(release_year_dict.keys())

# Get all the values in dictionary
print(release_year_dict.values())

# Append value with key into dictionary
release_year_dict['Graduation'] = '2007'
print(release_year_dict)

# Delete entries by key
del(release_year_dict['Thriller'])
del(release_year_dict['Graduation'])
print(release_year_dict)

# Verify the key is in the dictionary
print('The Bodyguard' in release_year_dict)

"""
{'key1': 1, 'key2': '2', 'key3': [3, 3, 3], 'key4': (4, 4, 4), 'key5': 5, (0, 1): 6}
1
6
{'Thriller': '1982', 'Back in Black': '1980', 'The Dark Side of the Moon': '1973', 'The Bodyguard': '1992', 'Bat Out of Hell': '1977', 'Their Greatest Hits (1971-1975)': '1976', 'Saturday Night Fever': '1977', 'Rumours': '1977'}
1982
dict_keys(['Thriller', 'Back in Black', 'The Dark Side of the Moon', 'The Bodyguard', 'Bat Out of Hell', 'Their Greatest Hits (1971-1975)', 'Saturday Night Fever', 'Rumours'])
dict_values(['1982', '1980', '1973', '1992', '1977', '1976', '1977', '1977'])
{'Thriller': '1982', 'Back in Black': '1980', 'The Dark Side of the Moon': '1973', 'The Bodyguard': '1992', 'Bat Out of Hell': '1977', 'Their Greatest Hits (1971-1975)': '1976', 'Saturday Night Fever': '1977', 'Rumours': '1977', 'Graduation': '2007'}
{'Back in Black': '1980', 'The Dark Side of the Moon': '1973', 'The Bodyguard': '1992', 'Bat Out of Hell': '1977', 'Their Greatest Hits (1971-1975)': '1976', 'Saturday Night Fever': '1977', 'Rumours': '1977'}
True


** Process exited - Return Code: 0 **
Press Enter to exit terminal
"""
