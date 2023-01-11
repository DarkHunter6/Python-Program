print('# ----------- EVEN AND ODD NUMBER DETECTION ------------ #')

def collatz(Number):

    if Number % 2 == 0:    
        print('This Number Is Even Number')
    #Number = int(input())

    if Number % 2 == 1:
        print('This Number Is Odd Number')
    #Number = int(input())

print(collatz(int(input())))