Details = {'Name' : 'Tushar Paul', 'Address' : 'Kholta Chakpost', 'Dist' : 'Coochbehar', 'P.O' : 'Kholta', 'Pin' : 736121}
Details_2 = {1234 : 'Tushar Paul', 5678 : 'Kholta Chakpost', 9101112 : 'Coochbehar', 13141516 : 'Kholta', 17181920 : 736121}
print(type(Details), Details)
print(type(Details_2), Details_2) # Dictionary Can Use Integer & String Both Type Of Keys--- 

# ------------- Dictionary Vs List ---------------- #

List_1 = ['Bugatti', 'Lamborghini', 'Nissna', 'Pagani', 'Ford']
List_2 = ['Lamborghini', 'Bugatti', 'Pagani', 'Ford', 'Nissna']
print(List_1 == List_2) # The Items Allignment Of Two Lists Will Be Same, Then It Will Be True, Otherwise It Will Be False

Dictionary_1 = {'Name' : 'Tushar Paul', 'Address' : 'Kholta Chakpost', 'Dist' : 'Coochbehar', 'P.O' : 'Kholta', 'Pin' : 736121}
Dictionary_2 = {'Address' : 'Kholta Chakpost', 'Name' : 'Tushar Paul',  'Pin' : 736121, 'Dist' : 'Coochbehar',  'P.O' : 'Kholta'}
print(Dictionary_1 == Dictionary_2) # Dosen't Matter The Items Allignment Of The Dictionaries Will Be Same Or Not, If The Data Will Be Still In Another Dictionary, 
                                    # It Will Be True.
print(Dictionary_1.items()) # Show The Multiple Key Values Separately
del[Dictionary_1['Name']] # Delete Any Key Values With It
print(Dictionary_1)