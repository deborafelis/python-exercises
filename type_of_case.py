def test_case():
    text = 'Hello, World!'
    print(text)
    print(text.lower())
    print(text.upper())
    print(text.capitalize())
    print(text.swapcase())
    print(text.count('l'))
    
def type_of_case():
    user_text = input('Write anything and see what happens: ')
    if user_text.isupper():
        print('Upper case letters.')
    elif user_text.islower():
        print('Lower case letters.')
    else:
        print('Mixed types of case.')
type_of_case()

