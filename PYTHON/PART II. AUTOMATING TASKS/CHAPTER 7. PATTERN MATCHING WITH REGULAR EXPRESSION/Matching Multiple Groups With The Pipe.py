import re

Name = re.compile(r'Tushar Paul | DarkEagle')
Group_1 = Name.search('Tushar Paul And DarkEagle') # Get The First String Search
print(Group_1.group())

# Name_1 = Name.search('DarkEagle And Tushar Paul')
# print(Name_1.group()) # According To Book