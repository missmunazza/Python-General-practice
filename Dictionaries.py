dict1 = {'a' : 1, 'b':2, 'c':3}
print(dict1)
dict1 = {'a' : 1, 'a' : 1, 'b':2, 'c':3}
print(dict1)
print(dict1['a'])
#nested dict
dict2 = {'name' : 'ali', 'age' : 39, 'email': 'ali@gmail.com'}
print(dict2['name']) #accessing
dict3 = {'name' : 'ali', 'age' : 39, 'email': 'ali@gmail.com', 'study': {'subject': 'math', 'marks': 90}}
print(dict3)
dict2['name'] = 'sarfraz'
print(dict2)
print(dict2.get('a'))
#getting values
x = dict3.values()
print(x)
#removing items
dict2.pop("age")
print(dict2)

#get the values and get the second highest value

current_grade = {2022: '80%', 2023:'90%', 2024:'70%', 2025:'85%'}
current_grade = list(current_grade.values())
print(current_grade)
sorted_values = sorted(current_grade, reverse=True)
print(sorted_values[1])

current_grade = {2022: '80%', 2023:'90%', 2024:'70%', 2025:'85%'}
current_grade = list(current_grade.values())
print(current_grade)
new_sorted = current_grade.sort()
print(new_sorted[1])