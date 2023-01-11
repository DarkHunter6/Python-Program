Car = 'Bugatti Is A Super Car'
Car_2 = Car[: 11] + 'The' + Car[12 : 22] 
print(Car, Car_2)

# --- Proper Modify The Values In The List ---

Name = ['Tushar', 'Sharmistha', 'Koushik', 'Sourav', 'Anirban', 'Subhradip']
del Name[0]
del Name[0]
del Name[0]
del Name[0]
del Name[0]
del Name[0]
Name.append(str(input()))
Name.append(str(input()))
Name.append(str(input()))
Name.append(str(input()))
Name.append(str(input()))
Name.append(str(input()))
print(Name)