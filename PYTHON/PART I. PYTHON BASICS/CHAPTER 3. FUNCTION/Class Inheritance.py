class Sports_Car:
    
    def __init__(Self):
        Self.Big_Boy_Toys = 'Bugatti'
        Self.Cars()
        
    def Cars(Self):  # Cars() -> Normal Function // Object.Cars() -> Method // You Can Also Call Or Pass Any Class Into The Parameter
        print('Sui Sui Sui Sui Sui')
        
My_Cars = Sports_Car() # Pass The Sports_Car Class
print(My_Cars.Big_Boy_Toys)

print('+ + + + + + + + + + Create A Child Class And + + + + + + + + + + ')

class Imported_Cars(Sports_Car): # What We Have Done Here Is Called Inheritance. We Call The Another Class And Simply Pass 
                                 # It Through The Child Class. 
    pass
My_Cars = Imported_Cars()
print(My_Cars.Big_Boy_Toys)
