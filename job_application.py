def qualified_candidates():
    portuguese = input('Do you speak Portuguese? ')
    spanish = input('Do you speak Spanish? ')
    if portuguese.lower() == 'yes' and spanish.lower() == 'yes':
        print(f'You\'re qualified for this job.')
    else:
        print(f'You\'re not qualified for this job.')

