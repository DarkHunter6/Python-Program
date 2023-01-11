Name = ''
while not Name:
    print('Enter Your Name')
    Name = input()
    print(Name + ' How Many Programs Can You Run At A Time')
    Programs = str(input())
    if Programs:
        print(Programs + ', Make Sure You Can Complete This Programs')