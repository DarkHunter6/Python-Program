Details = "I'm Nobody And You Are A Fucking Lier"

Details_1 = Details[12]                  # ---|
print('Original Data Is : ' + Details)   #    |---> [ Indexing Strings ]
print('Indexing Data Is : ' + Details_1) # ---|

Details_2 = Details[ 10 : -10 ] # [ Slicing Starts And Counts From 1, Not From 0 ] 
                        # [ Positive Value In Right : How Many Characters Will Be Shown From 'Left Side' ]
                        # [ Negative Value In Right : How Many Characters Will Be Deleted From 'Right Side' ]
                        # [ Positive Value In Left : How Many Characters Will Be Deleted From Left Side ]
                        # [ Negative Value In Left : How Many Characters Will Be Shown From Right Side ]
print(Details_2)     