import random
import string

def generate_password(length):
    """
    Generate a password of the specified length using a combination of random characters.
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    """
    Main function to prompt the user for the desired password length and generate a password.
    """
    print("Password Generator")
    print("------------------")

    # Prompt the user to specify the desired length of the password
    while True:
        try:
            length = int(input("Enter the desired length of the password (min 8 characters): "))
            if length < 8:
                print("Password length must be at least 8 characters.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    # Generate the password
    password = generate_password(length)

    # Display the generated password
    print("Generated Password:")
    print(password)

if __name__ == "__main__":
    main()
