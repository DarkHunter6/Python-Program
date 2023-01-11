Name = {'Name' : 'Tushar Paul', 'Roll' : 177580759, 'Address' : 'Kholta Chakpost', 'Dist' : 'Coochbehar'}
# print(Name.keys())
# print(Name.values())
# print(Name.items())

# print(list(Name.keys()))
# print(list(Name.values()))
# print(list(Name.items()))

for K, V in Name.items():
    print('Key : ' + K + ' Value : ' + str(V))
    
Hello = 'Tushar Paul' in Name.values()
print(Hello)