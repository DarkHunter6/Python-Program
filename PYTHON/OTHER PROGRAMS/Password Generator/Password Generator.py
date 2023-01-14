from random import*
import string

String_1 = list(string.ascii_uppercase) # A-Z
String_2 = list(string.ascii_lowercase) # a-z
String_3 = list(string.digits) # 0-9
String_4 = list(string.punctuation) # Special Characters

User_Input = int(input('How Many Characters Do You Want : '))

while True:

    try:
        
        if User_Input < 10:
            print('Your Number Should Be At Least 10 Characters')
            User_Input = int(input('Enter The Character Number What You Want : '))
        
        else:
            break
    
    except:
        print('Your Number Should Be At Least 10 Characters')
        User_Input = int(input('Enter The Character Number What You Want : '))
        
# Now Suffle Mean Mixing All The String_1, String_2, String_3 And String_4
shuffle(String_1)
shuffle(String_2)
shuffle(String_3)
shuffle(String_4)

Part_1 = round(User_Input * (30/100)) # String_1 And String_2 Each Characters Gonna Have 30% Of Password [Total = 60%]
Part_2 = round(User_Input * (20/100)) # String_3 And Strinf_4 Each Characters Gonna Have 20% Of Password [Total = 40%]

Result = []

for Ps in range(Part_1): # 1
    Result.append(String_1[Ps]) # 1
    Result.append(String_2[Ps]) # 1
    
for Ps in range(Part_2): # 2    
    Result.append(String_3[Ps]) # 2
    Result.append(String_4[Ps]) # 2
    
shuffle(Result) # 3
Password = ''.join(Result) # 4

print('Your Password Is : ' + str(Password))

# ========================== Defination Of This Code ========================

# 1. We Run A Loop Basis Of Part_1 Variable Over The String_1 And String_2 Variable To Get The Exact Number Of 
# Characters And append() Put The Characters Into The 'Result' From The Last Line Bais Of Index Number [Ps], 
# As You Can See We Define The Index Number To The String Variable. 

# 2. Same As 1, Just Has The Difference In Numbers Of Characters. Set The Breakpoints In Loops And See.
# 3. Then You Shake The Characters And Make A 'Password Shake' Like 'Milk Shake'.
# 4. And Finally Add Them With .join().