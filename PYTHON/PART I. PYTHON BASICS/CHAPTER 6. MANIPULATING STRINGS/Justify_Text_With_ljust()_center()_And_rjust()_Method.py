# Name = 'Tushar Paul'
# print(Name.rjust(20, '+'))
# print(Name.ljust(20, '+'))
# print(Name.center(20, '+'))

# --------------------- PICNIC ------------------------ #

def Picnic(ItemsDict, LeftWidth, RightWidth):
    print('PICNIC ITEMS'.center(LeftWidth + RightWidth, '-'))
    for K,V in ItemsDict.items():
        print(K.ljust(LeftWidth, '.') + str(V).rjust(RightWidth))
Picnic_Items = {'Bread' : 10, 'Egg' : 10, 'Rosogolla' : 10}
Picnic(Picnic_Items, 12, 5)

print('========================== NEW OUTPUT =============================')

def MyCars(Cars, Left, Right):
    print('Cars_List'.center(Left + Right, '-'))
    for K,V in Cars.items():
        print(K.ljust(Left, '.') + str(V).rjust(Right))
Cars_3 = {'Nissan GTR Skyline' : 10, 'Bugatti Divo' : 10, 'Rols Royce' : 10}
MyCars(Cars_3, 30, 5)

print('========================== NEW OUTPUT =============================')

def Friends(Name, Right, Left):
    print('FRIEND LIST'.center(Left + Right) + 'AGE'.rjust(Right))
    print('--------------------------------')
    for K,V in Name.items():
        print(K.ljust(Right, '.') + str(V).rjust(Right))
My_Friends = {'Tushar Paul' : '-> 23', 'Koushik Saha' : '-> 25', 'Sourav Das' : '-> 22'}
Friends(My_Friends, 15, 0)