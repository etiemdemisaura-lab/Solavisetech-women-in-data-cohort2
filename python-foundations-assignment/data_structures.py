# Favourite tools

Tools = {'anaconda', 'Github', 'git'}
tools.append('git')
tools.remove('anaconda')
print("Favorite Tools:", tools)

# Student scores

Scores = [25, 30, 28, 35, 40]
print(Scores)
print(highest_score)
print(lowest_score)
print(average_score)

Shopping list manager

 Unique

shopping_list.append('sugar')
shopping_list.append('onions')
shopping_list.append('salt')
print(shopping_list)

# Country Capitals

countries = (('Cameroon', 'Yaounde'),
              ('Ghana', 'Accra'),
              ('Nigeria', 'Abuja'))
print("Country Capitals:", countries)

# Unique Visitors

visitors = ['tina', 'alex', 'meindl', 'meindl']
unique_visitors = set(visitors)
print(unique_visitors)

# Common skills

skills1 = ['biology', 'chemistry', 'physics']
skills2 = ['math', 'computer science', 'biology']

common_skills = set(skills1) .intersection(set(skills2))
print(common_skills)

# Student record

name = 'Sandra'
height = 1.65
age = 30
student_record = (name, height, age)
print(student_record)

# Mini contact book

contact = {'tina': '123-456-7890', 'bob': '987-654-3210'}
print(contact['tina'])
search = input('Enter a name to search for: ')
print(contact[search])
if search in contact:
    print(contact[search])
else:
    print('Name not found in contact list.')






