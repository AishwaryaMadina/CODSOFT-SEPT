import random

def generate_password(length, use_uppercase, use_digits, use_special_chars):
    characters = "abcdefghijklmnopqrstuvwxyz"
    if use_uppercase: characters += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if use_digits: characters += "0123456789"
    if use_special_chars: characters += "!@#$%^&*()_+-=[]{}|;:'\",.<>/?"

    if not any([use_uppercase, use_digits, use_special_chars]):
        return "Include at least one of uppercase letters, digits, or special characters."

    return ''.join(random.choice(characters) for _ in range(length))

if __name__ == "__main__":
    print("Welcome to the Password Generator!")
    length = int(input("Enter the desired password length: "))
    use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == "yes"
    use_digits = input("Include digits? (yes/no): ").lower() == "yes"
    use_special_chars = input("Include special characters? (yes/no): ").lower() == "yes"

    password = generate_password(length, use_uppercase, use_digits, use_special_chars)
    print("Generated Password:", password)
