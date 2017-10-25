from dictionary import lookup

# Load data
running = True


def terminate():
    keep_going = input('Do you want to lookup another word? [y/n] ')

    if keep_going == 'y':
        return True
    elif keep_going == 'n':
        return False

    print('You have to answer with y or n')
    return terminate()


while running:
    user_input = input('What word are you looking for? ')

    lookup(user_input)

    running = terminate()

print("Goodbye")
