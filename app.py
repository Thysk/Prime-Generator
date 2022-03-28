import prime_find


# Main loop for program, generates the CLI menu to interact with code.
def menu():
    user_options = {
        'r': prime_find.return_primes,
        'f': prime_find.find_primes_workflow
    }
    USER_CHOICE = """What would you like to do?
'r' : Returns all primes found
or
'f' : Find more primes: """
    user_input = input(USER_CHOICE)

    while True:
        if user_input in user_options:
            if user_input == 'r':
                # Print the returned primes, can be changed later to something else
                selected_function = user_options[user_input]
                print(selected_function())
            else:
                selected_function = user_options[user_input]
                selected_function()
        else:
            print("Input not recognised, please try again.")
        user_input = input(USER_CHOICE)


menu()
