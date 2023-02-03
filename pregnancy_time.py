def pregnancy_time():
    weeks = int(input('How many weeks have you been expecting?'))
    if weeks == 41 :
       print(f'Your pregnancy time is {weeks}. If you deliver now, the birth will be late-term.')
    elif weeks >= 44:
        print(f'You should see a doctor.')
    elif weeks >= 42:
        print(f'Your pregnancy time is {weeks}. If you deliver now, the birth will be postterm.')
    elif weeks <= 34 and weeks >= 37:
        print(f'Your pregnancy time is {weeks}. If you deliver now, the birth will be late preterm.')
    elif weeks >28 and weeks <= 33:
        print(f'Your pregnancy time is {weeks}. If you deliver now, the birth will be moderatety preterm.')
    elif weeks <0:
        print(f'Invalid')
    elif weeks <1:
        print(f'You\'re not pregnant yet.') 
    elif weeks <=28:
        print(f'Your pregnancy time is {weeks}. If you deliver now, the birth will be extremely preterm.')
    else:
        print(f'Your pregnancy time is {weeks}. If you deliver now, the birth will be full term.')

pregnancy_time()
