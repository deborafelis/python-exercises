def calculate_total_tiles():
    wall1 = 15*10
    wall2 = 13*10
    total_tiles = print(wall1+wall2)

def compare_height_to_messi():
    messi = 1.69
    yours = float(input('Inform your height: '))
    if yours >= 1.70:
        print(f'You\'re taller than Lionel Messi.')
    elif yours == 1.69:
        print(f'You\'re as tall as Lionel Messi.')
    else:
        print(f'You\'re shorter than Lionel Messi.')
        
def calculate_change2():
    money = 20
    popcorn = 2.75
    juice = 2
    candies = 0.50
    change = print(money - popcorn - juice- candies)

def calculate_change():
    money = float(input('Inform your current money: '))
    expense = float(input('Inform the expense: '))
    change = money - expense
    print(f'You have ${money:.2f} and you\'re spending ${expense:.2f}. Your change is {change:.2f}.') 
                
