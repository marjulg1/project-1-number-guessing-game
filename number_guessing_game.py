import random


# Function to check if the user_input_number is between range, if not raise a value exeption
def check_value(low, high, user_value):
    if low <= user_value <= high:
        return True
    else:
        raise ValueError()


# Function to get a hint
def get_a_hint(user_input, computer_number):
    if user_input > computer_number:
        return "Try a lower number."
    else:
        return "Try a higher number."


# Function for main_menu
def main_menu_print():
    print("Hey dude... Welcome to the exotic game of number guessing!")
    print("Please provide a number between 0 and 10 and see in how many attempts you can guess what I have.")
    print("If you want to exit please type 'x'.")
    print("")


def play_again_check(user_input):
    while True:
        if user_input.upper() == "Y":
            return True
        elif user_input.upper() == "N":
            return False
        else:
            user_input = input("Invalid value. Please enter 'Y' or 'N': ")
            continue


def start_game():
    # Start the game with a highscore of 100. The user would never reach this number, worst case scenario would be 10 attempts.
    high_score = 100
    # create an empty list for temporal user attempts.
    user_input_lst = []
    # generate a random number
    computer_number = random.randint(0, 10)
    # call print menu function
    main_menu_print()
    # Loop for user attempts. It would break if the user hits 'x' anytime, or if the user hits 'n' when the program asks "do you want to plan again?
    while True:
        try:
            user_input = input("Your guess: ")
            # if the user hit 'x' program break, if not check for integer number, value range, and append user_attemp in a list
            if type(user_input) == str and user_input.upper() == 'X':
                print("We hope you've enjoyed the game. See you next time.")
                break
            else:
                user_input = int(user_input)
                check_value(0, 10, user_input)
                user_input_lst.append(user_input)

        except ValueError:
            # ValueError handling for lines 50 and 51. Line 51 call a funtion to verify if the number is in range, if not throws a ValueError
            print("The value is not in a valid range. You should enter an integer number between 0 and 10")
            input("Please hit any key to resume.")

        else:
            if computer_number == user_input:
                # User sucess hit
                if len(user_input_lst) < high_score:
                    high_score = len(user_input_lst)

                print("Congratulations, you won !")
                print("You have made {} attempts. Your choices: ".format(len(user_input_lst)))
                # additional print of user attempts
                for choice in user_input_lst:
                    print("- {}".format(choice))
                print("")
                # program asks if the user want to play again. The function returns True (y) or False (n)
                input_play_again = play_again_check(input("Do you want to play again? Y/N : "))

                if input_play_again:
                    # If the user wants to play again:
                    main_menu_print()
                    print("Your high score is: {}. Try to lower it!".format(high_score))
                    # New random number and clear list of attempts
                    computer_number = random.randint(0, 10)
                    user_input_lst = []
                    continue

                else:
                    # If the user does not want to play anymore. Print highest score and exits.
                    print("Your highest score was {}. Best luck next time!".format(high_score))
                    break

            else:
                # The user missed. Print a hint.
                print(get_a_hint(user_input, computer_number))


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()

