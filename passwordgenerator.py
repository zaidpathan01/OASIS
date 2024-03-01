import random
import string


def generate_password(length, lowercase, uppercase, numbers, symbols):
    """Generates a random password based on user-defined criteria.

    Args:
        length (int): Desired password length (must be between 8 and 64).
        lowercase (bool): Include lowercase letters (True/False).
        uppercase (bool): Include uppercase letters (True/False).
        numbers (bool): Include numbers (True/False).
        symbols (bool): Include symbols (True/False).

    Returns:
        str: The generated password.
    """

    if length <= 0 or length > 64:
        raise ValueError("Password length must be between 8 and 64 characters.")

    char_sets = []
    if lowercase:
        char_sets.append(string.ascii_lowercase)
    if uppercase:
        char_sets.append(string.ascii_uppercase)
    if numbers:
        char_sets.append(string.digits)
    if symbols:
        char_sets.append(string.punctuation)

    if not char_sets:
        raise ValueError("Please select at least one character type.")

    characters = "".join(char_sets)
    password = "".join(random.sample(characters, length))
    return password


def main():
    try:
        while True:
            length = int(input("Enter desired password length (8-64): "))
            if 8 <= length <= 64:
                break
            else:
                print("Invalid length. Please enter a number between 8 and 64.")

        lowercase = input("Include lowercase letters (y/n)? ").upper() in ("Y", "YES")
        uppercase = input("Include uppercase letters (y/n)? ").upper() in ("Y", "YES")
        numbers = input("Include numbers (y/n)? ").upper() in ("Y", "YES")
        symbols = input("Include symbols (y/n)? ").upper() in ("Y", "YES")

        password = generate_password(length, lowercase, uppercase, numbers, symbols)
        print(f"Your generated password: {password}")

    except (ValueError, IndexError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
