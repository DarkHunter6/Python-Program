Tic_Tac_Toe = {'Top-L' : ' ', 'Top-M' : ' ', 'Top-R' : '  ',
               'Mid-L' : ' ', 'Mid-M' : ' ', 'Mid-R' : ' ',
               'Low-L' : ' ', 'Low-M' : ' ', 'Low-R' : ' '}
def Board(Tic_Tac_Toe):
    print(Tic_Tac_Toe['Top-L'] + ' | ' + Tic_Tac_Toe['Top-M'] + ' | ' + Tic_Tac_Toe['Top-R'])
    print('---------')  
     
    print(Tic_Tac_Toe['Mid-L'] + ' | ' + Tic_Tac_Toe['Mid-M'] + ' | ' + Tic_Tac_Toe['Mid-R']) 
    print('---------')   
    
    print(Tic_Tac_Toe['Low-L'] + ' | ' + Tic_Tac_Toe['Low-M'] + ' | ' + Tic_Tac_Toe['Low-R']) 


print('* * * * * START THE GAME * * * * *')
Turn = 'X'
for i in range(9): 
    Board(Tic_Tac_Toe) 
    print('Turn For Player ' + ' Choose ' + '[' + Turn + ']' + ' ...Where Do You Want To Palce It ?')  
    Move = input()
    Tic_Tac_Toe[Move] = Turn 
    if Turn == 'X':
        Turn = 'O'
    else:
        Turn = 'X'
Board(Tic_Tac_Toe)