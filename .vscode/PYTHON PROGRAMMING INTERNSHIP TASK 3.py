import random
import string

def generate_password(length):
    # Define the character sets
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

def main():
    # Prompt the user to specify the desired length of the password
    try:
        length = int(input("Enter the desired length of the password: "))
        
        if length < 1:
            print("Error: Password length must be at least 1.")
            return
        
        # Generate the password
        password = generate_password(length)
        
        # Display the generated password
        print(f"Generated password: {password}")
        
    except ValueError:
        print("Error: Please enter a valid number for the password length.")

# Run the main function
if __name__ == "__main__":
    main()
