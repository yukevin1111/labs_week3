user_replay_input = ''

print('Welcome to the Flarsheim Guesser!')

# Repeats as long as the lowercased user_replay_input does not equal n.
while user_replay_input.lower() != 'n':

    # Resets user_replay_input, num_list, and remove_list for the new loop.
    user_replay_input = ''
    num_list = []
    remove_list = []

    print('\nPlease think of a number between and including 1 and 100.\n')

    # Asks for the expected remainder when dividing by 3, and appends the numbers that
    # has the remainder equal to the entered remainder into num_list.
    remainder = int(input('What is the remainder when your number is divided by 3 ? '))
    for num in range(1,101):
        while remainder < 0 or remainder >= 3:
            if remainder < 0:
                print('The value entered must be 0 or greater')
            elif remainder >= 3:
                print('the value entered must be less than 3')
            remainder = int(input('What is the remainder when your number is divided by 3 ? '))
        if num % 3 == remainder:
            num_list.append(num)

    # Asks for the expected remainder when dividing by 5, and appends the numbers that
    # has the remainder NOT equal to the entered remainder into remove_list.
    remainder = int(input('\nWhat is the remainder when your number is divide by 5 ? '))
    for item in num_list:
        while remainder < 0 or remainder >= 5:
            if remainder < 0:
                print('The value entered must be 0 or greater')
            elif remainder >= 5:
                print('The value entered must be less than 5')
            remainder = int(input('What is the remainder when your number is divide by 5 ? '))
        if item % 5 != remainder:
            remove_list.append(item)

    # Asks for the expected remainder when dividing by 7, and appends the numbers that
    # has the remainder NOT equal to the entered remainder into remove_list.
    remainder = int(input('\nWhat is the remainder when your number is divided by 7 ? '))
    for item in num_list:
        while remainder < 0 or remainder >= 7:
            if remainder < 0:
                print('The value entered must be 0 or greater')
            elif remainder >= 7:
                print('The value entered must be less than 7')
            remainder = int(input('What is the remainder when your number is divide by 7 ? '))
        if item % 7 != remainder:
            remove_list.append(item)

    # Goes through each item in remove_list. If that item exists in num_list, remove,
    # and if the item does not exist, pass.
    for item in remove_list:
        if item in num_list:
            num_list.remove(item)
        else:
            pass

    # This is in case there were no numbers remaining in num_list.
    if len(num_list) == 0:
        num_list.append('nonexistant or out of range.')

    # Print statement for output
    print('Your number was', num_list[0],'\nHow amazing is that?\n')

    # Asks user for a valid input, until vaild input is inputted.
    while user_replay_input.lower() != 'y' and user_replay_input.lower() != 'n':
        user_replay_input = input('Do you want to play again? Y to continue, N to quit ==> ')
