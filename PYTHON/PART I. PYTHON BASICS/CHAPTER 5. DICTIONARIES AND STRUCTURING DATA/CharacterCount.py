from pprint import*
Message = 'Hello, This Is FSociety And You Are Now In Our Custody. So, Do Not Try To Escape From Here Because You Can Not Do This...'
Count = {}

for character in Message:
    Count.setdefault(character, 0)
    Count[character] = Count[character] + 1
    
pprint((Count)) # Pretty Printing