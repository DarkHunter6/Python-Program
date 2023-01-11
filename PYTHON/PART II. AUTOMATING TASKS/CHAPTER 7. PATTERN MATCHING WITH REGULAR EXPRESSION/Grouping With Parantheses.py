import re

Phone_Number = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
Number = Phone_Number.search('My Phone Number Is 816-758-0245')
AreaCode, MainNumber, AssHole = Number.groups()
print(AreaCode)
print(MainNumber)
print(AssHole)
# PhoneNumberRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
# mobile = PhoneNumberRegex.search('My Number Is 816 758-0245. ')
# print(mobile.group(1))
