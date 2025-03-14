def display_menu() -> None:
    """
    Display the menu options for the user.
    """
    print("\nMenu:")
    print("1. Greet User")
    print("2. Check Even/Odd")
    print("3. Exit")


def greet_user() -> None:
    """
    Print a greeting message.
    """
    print("Hello! Welcome!")


def get_integer_input() -> int:
    """
    Prompt the user to enter an integer and validate the input.
    
    Returns:
        int: The valid integer input.
    """
    while True:
        try:
            number = int(input("Enter an integer: "))
            return number
        except ValueError:
            print("Error: Invalid input. Please enter a valid integer.")


def check_even_odd(number: int) -> str:
    """
    Determine whether a given number is even or odd.

    Args:
        number (int): The number to check.

    Returns:
        str: A formatted message indicating whether the number is even or odd.
    """
    if number % 2 == 0:
        return f"{number} is an Even number."
    else:
        return f"{number} is an Odd number."


def even_odd_checker_action() -> None:
    """
    Handle the logic for getting user input and checking if it's even or odd.
    """
    num = get_integer_input()
    print(check_even_odd(num))


def handle_menu_choice(choice: int) -> bool:
    """
    Execute the corresponding action based on the user's menu choice.

    Args:
        choice (int): The menu option selected.

    Returns:
        bool: True if the user chooses to exit, False otherwise.
    """
    if choice == 1:
        greet_user()
    elif choice == 2:
        even_odd_checker_action()
    elif choice == 3:
        print("Exiting program. Goodbye!")
        return True
    else:
        print("Error: Invalid choice. Please select a valid option (1-3).")
    return False


# Main Program Flow
if __name__ == "__main__":
    while True:
        display_menu()
        try:
            user_choice = int(input("Enter your choice (1-3): "))
            if handle_menu_choice(user_choice):
                break
        except ValueError:
            print("Error: Invalid input. Please enter a number between 1 and 3.")