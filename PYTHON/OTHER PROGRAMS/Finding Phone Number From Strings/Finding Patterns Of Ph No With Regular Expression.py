import re

# ================================================================= [Program 1]
# MyNum = re.compile(r'\d{3}-\d{3}-\d{4}')
# PhNo = MyNum.search('My Number Is 978-675-0897')
# print('Phone Number Found : ' + PhNo.group())

# ================================================================= [Program 2]

# MyNum = re.compile('\d\d\d-\d\d\d-\d\d\d\d')
# PhNo = MyNum.search('My Number Is 978-675-0897')
# print('Phone Number Found : ' + PhNo.group())

# ================================================================= [Program 3]

# MyNum = re.compile('\d{3}-\d{3}-\d{4}')
# PhNo = MyNum.search('My Number Is 978-675-0897')
# print('Phone Number Found : ' + PhNo.group())

#================================================================== [Program 4]

# MyNum = re.compile('(\d\d\d)-(\d\d\d-\d\d\d\d)')
# PhNo = MyNum.search('My Number Is 978-675-0897')
# print('Phone Number Found : ' + PhNo.group(1))
# print('Phone Number Found : ' + PhNo.group(2))

# ================================================================= [Program 5]

# MyNum = re.compile('(\d\d\d)-(\d\d\d-\d\d\d\d)')
# PhNo = MyNum.search('My Number Is 978-675-0897')
# AreaCode, MainNumber = PhNo.groups()
# print(AreaCode)
# print(MainNumber)

# *******************************************************************
