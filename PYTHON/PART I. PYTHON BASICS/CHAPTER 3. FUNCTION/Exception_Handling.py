def Math(DividedBy):
    try:
        return 42 / DividedBy
    except ZeroDivisionError:
        print('Error : Invalid Argument')

print(Math(int(input())))
print(Math(int(input())))
print(Math(int(input())))
print(Math(int(input())))