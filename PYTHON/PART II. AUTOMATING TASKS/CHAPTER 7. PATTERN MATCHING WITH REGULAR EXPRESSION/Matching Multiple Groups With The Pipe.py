import re

Name = re.compile(r'Tushar Paul | DarkEagle')
Group_1 = Name.search('Tushar Paul And DarkEagle') # Get The First String Search
print(Group_1.group())
