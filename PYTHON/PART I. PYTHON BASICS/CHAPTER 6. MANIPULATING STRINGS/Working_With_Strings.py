# -------------------- Working With Strings ------------------------

# [ Double Quotes ]
Details = "My Name Is Tushar Paul, Yes It's Me"
print(Details)

# [ Escape Characters | Types : ( \', \", \n, \t, \\ ) ]
Details_1 = 'My Name Is Tushar Paul, Yes It\'s Me'
print(Details_1)

# [ Raw Strings - Escape Characters Are Not Usable While Using Raw Strings ]
print(r'My Name Is Tushar Paul, Yes It\'s Me')

# [ Multiline Strings With Triple Quotes]
Details_2 = ''' Dear AMD,
            This Is An Honor To Work With You.
                                                Your Best User
                                                 Tushar Paul'''
print(Details_2)

# [ Multiline Comments ]
Der = """Dear AMD,
            This Is An Honor To Work With You.
                                                Your Best User
                                                 Tushar Paul
"""
def Hacking():
    Des = """What The Hell Is Hacking() Function Doing Here...!
"""
    print(Der)
Hacking()