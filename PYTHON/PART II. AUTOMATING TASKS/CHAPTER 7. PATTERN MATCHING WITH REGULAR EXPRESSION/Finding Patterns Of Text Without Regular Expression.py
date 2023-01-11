def IsPhoneNumber(Text):
    if len(Text) != 12:
        return False
    # ------------------------- #
    for i in range(0, 3):
        if not Text[i].isdecimal():
            return False
    # ------------------------- #
    if Text[3] != '-': # Because 0, 1, 2 And In Position 3 If There Is Not Any '-' Sign, It Returns False Otherwise True.
        return False
    # ------------------------- #
    for i in range(4, 7):
        if not Text[i].isdecimal():
            return False
    # ------------------------- #
    if Text[7] != '-':
        return False
    # ------------------------- #
    for i in range(8, 12):
        if not Text[i].isdecimal():
            return False
    # ------------------------- #
    return True
# print('Enter Anym Phone Number')
# print(IsPhoneNumber(str(input())))

Message = 'Call Me At 863-781-3299 Tommorrow. 816-758-0245 Is My Personal Number'
for i in range(len(Message)):
    Find = Message[i : i + 12]
    if IsPhoneNumber(Find):
        print('Phone Number Found : ' + Find)
print('Done')