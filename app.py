import prime_find


# Main loop for program, generates the CLI menu to interact with code.
def app_menu(user_input: str = None, upper_bound: int = None):
    user_options = {
        'r': prime_find.return_primes,
        'f': prime_find.find_primes_workflow
    }
    USER_CHOICE = """What would you like to do?
'r' : Returns all primes found
or
'f' : Find more primes: """

# menu work around for automation
    if user_input:
        if user_input == 'r':
            # Print the returned primes, can be changed later
            selected_function = user_options[user_input]
            return(selected_function())
        elif user_input == 'f':
            selected_function = user_options[user_input]
            selected_function(upper_bound)
    else:
        user_input = input(USER_CHOICE)
        # Human menu in a loop
        while True:
            if user_input in user_options:
                if user_input == 'r':
                    # Print the returned primes, can be changed later
                    selected_function = user_options[user_input]
                    print(selected_function())
                elif user_input == 'f':
                    selected_function = user_options[user_input]
                    selected_function()
            else:
                print("Input not recognised, please try again.")
            user_input = input(USER_CHOICE)


if __name__ == "__main__":
    app_menu()
