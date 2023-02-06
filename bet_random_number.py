def bet_random_number():
    import random
    number = random.randint(1,20)
    bet = int(input('Insert a number from 1 to 20: '))
    if number == bet:
              print(f'Yay! You got it right!')
    else:
        print(f'Sorry. You picked {bet} and {number} was drafted.')

