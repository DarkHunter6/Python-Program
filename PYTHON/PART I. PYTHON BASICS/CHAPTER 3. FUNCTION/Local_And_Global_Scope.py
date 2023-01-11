# (Local Variable Cannot Be Use In Global Scope --)

# def Spam():
#     Eggs = 10
    
# Spam()
# print(Eggs)

# ---------------------------------------------- #

# (Local Scopes Cannot Use Variables In Other Local Scope --)

# def Spam():
#     Eggs = 10
#     Spam1()
#     print(Eggs)
    
# def Spam1():
#     Eggs = 20
#     print(Eggs)
        
# Spam()

# ---------------------------------------- #

# (Global Variable Can Be Read From A Local Scope)

# def Spam():
#     print(Eggs)
# Eggs = 10 # Python Considers It As Global Variable
# Spam()
# print(Eggs)

# --------------------------------------- #

# (Local And Global Variable With The Same Name)

# def Spam():
#     Eggs = 'Spam Local Scope'
#     print(Eggs)
    
# def Spam2():
#     Eggs = 'Spam2 Local Scope' # Same Variable Name Like Previous One
#     print(Eggs)
#     Spam()
    
# Eggs = 'This Is Global Scope'
# print(Eggs)
# Spam2()

# ------------------------------------ #

# (The Global Statement)

# global Eggs # global Keyword Use To Declear A Variable As A Global Variable And Never Use This Same Name Variable In Other Local Scope.
# Eggs = 'Global Variable Eggs'
    
# def Spam2():
#     Eggs = 20

# print(Eggs)

# ------------------------------------- #

# def Spam():
#     print(Eggs)
#     Eggs = 10
# Eggs = 20
# Spam()

# --------------------------------- #