def PrimeNumber():
    Number = input('Enter Any Number : ')
    if int(Number) % 2 == 0:
        print('The Number Is Not Prime')
    else:
        print('The Number Is Prime')
PrimeNumber()