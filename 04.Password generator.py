import random
import string

def generate_password():
    print("--- Custom Password Generator ---")
    
    try:
        length = int(input("Enter desired password length: "))
        
        use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
        use_digits = input("Include numbers? (y/n): ").lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

        char_pool = ""
        if use_upper:
            char_pool += string.ascii_uppercase
        if use_lower:
            char_pool += string.ascii_lowercase
        if use_digits:
            char_pool += string.digits
        if use_symbols:
            char_pool += string.punctuation

        if not char_pool:
            print("Error: You must select at least one character type.")
            return

        password = "".join(random.choice(char_pool) for _ in range(length))
        
        print(f"\nYour Password: {password}")

    except ValueError:
        print("Please enter a valid number for the length.")

if __name__ == "__main__":
    generate_password()