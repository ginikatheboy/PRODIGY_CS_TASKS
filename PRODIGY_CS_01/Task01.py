# Function to encrypt the text using Caesar Cipher
def encrypt(text, shift):
    result = ""

    # Traverse through each character in the text
    for char in text:
        # Encrypt uppercase letters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase letters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        # If it's not a letter, add it directly (spaces, punctuation, etc.)
        else:
            result += char
    return result

# Function to decrypt the text using Caesar Cipher
def decrypt(text, shift):
    return encrypt(text, -shift)

# Main program
if __name__ == "__main__":
    print("Welcome to Caesar Cipher Encryption/Decryption Program!")
    
    # Ask for user input
    choice = input("Type 'e' to Encrypt or 'd' to Decrypt: ").lower()
    message = input("Enter your message: ")
    shift = int(input("Enter shift value (e.g., 3): "))

    if choice == 'e':
        encrypted_message = encrypt(message, shift)
        print(f"Encrypted Message: {encrypted_message}")
    elif choice == 'd':
        decrypted_message = decrypt(message, shift)
        print(f"Decrypted Message: {decrypted_message}")
    else:
        print("Invalid choice! Please select 'e' for encrypt or 'd' for decrypt.")
