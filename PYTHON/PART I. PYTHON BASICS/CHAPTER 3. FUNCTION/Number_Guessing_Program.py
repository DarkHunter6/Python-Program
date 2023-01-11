from random import*

print('# ----------- GUESS THE NUMBER ------------ #')
print('Take A Guess')
Number = int(input())
Number2 = randint(1, 5)

while Number < Number2:
    print('Your Guess Is Too Low')
    Number = int(input())

while Number > Number2:
    print('Your Guess Is Too High')
    Number = int(input())

if Number == Number2:
    print('# ----------- YOUR GUESS IS CORRECT -------------- #')