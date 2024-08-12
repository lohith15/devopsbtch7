import re

def check_password_strength(password):
    # Check if password meets the minimum length requirement
    if len(password) < 8:
        return False
    
    # Check if password contains both uppercase and lowercase letters
    if not re.search(r"[A-Z]", password) or not re.search(r"[a-z]", password):
        return False
    
    # Check if password contains at least one digit
    if not re.search(r"\d", password):
        return False
    
    # Check if password contains at least one special character
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False
    
    return True

def main():
    password = input("Enter a password to check its strength: ")
    
    if check_password_strength(password):
        print("Password is strong!")
    else:
        print("Password is weak! Please ensure it meets the following criteria:")
        print("- At least 8 characters long")
        print("- Contains both uppercase and lowercase letters")
        print("- Contains at least one digit (0-9)")
        print("- Contains at least one special character (e.g., !, @, #, $, %)")

if __name__ == "__main__":
    main()