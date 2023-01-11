from random import*

def QNA(Number):
    if Number == 1:
        return 'Tajmahal Is Situated In Agra'
    elif Number == 2:
        return 'Red Fort Is Situated In Delhi'
    elif Number == 3:
        return 'CharMinar Is Situated In Hydrabad'
    
# Answer = randint(1, 3)
# Answer1 = QNA(Answer)
# print(Answer1)

print(QNA(randint(1, 3)))