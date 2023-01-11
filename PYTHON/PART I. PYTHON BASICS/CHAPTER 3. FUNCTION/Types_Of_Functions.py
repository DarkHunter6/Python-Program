# ---------- No Argument With No Return Value ---------- #
def Cars():
    Car = 'Bugatti Is My Favourite Car'
    print(Car)
Cars()

# ---------- No Argument With Return Value ---------- #
def Cars_1():
    Car = 'Bugatti Is My Favourite Car'
    return Car
Cars()

# ---------- Argument With No Return Value ---------- #
def Cars(Cars_1):
    Car = 'Bugatti Is My Favourite Car'
    print(Car)
Cars('Bugatti Is My Favourite Car')

# ---------- With Argument And Return Value ---------- #
def Cars(Cars_1):
    Car = 'Bugatti Is My Favourite Car'
    return Car
print(Cars('Bugatti Is My Favourite Car'))