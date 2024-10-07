# Function to encrypt or decrypt an image
def process_image(image_path, output_path, key, mode):
    # Open the image file in binary mode
    file = open(image_path, "rb")
    image = file.read()
    file.close()

    # Convert image data to a bytearray for manipulation
    image = bytearray(image)

    # Encrypt or decrypt based on mode ('e' for encrypt, 'd' for decrypt)
    for i, j in enumerate(image):
        image[i] = j ^ key  # XOR operation with key for both encryption and decryption

    # Save the processed image to the output file
    file = open(output_path, "wb")
    file.write(image)
    file.close()

    print(f"Image successfully {'encrypted' if mode == 'e' else 'decrypted'} and saved to {output_path}!")

# Main logic
key = 48  # Key for XOR encryption/decryption

# Asking the user if they want to encrypt or decrypt the image
mode = input("Enter 'e' to encrypt or 'd' to decrypt: ").lower()

if mode == 'e':
    # Encrypting the image
    image_path = 'image.jpg'  # Input image file path
    output_path = 'encrypted.jpg'  # Output encrypted file path
    process_image(image_path, output_path, key, mode)

elif mode == 'd':
    # Decrypting the image
    image_path = 'encrypted.jpg'  # Input encrypted file path
    output_path = 'decrypted.jpg'  # Output decrypted file path
    process_image(image_path, output_path, key, mode)

else:
    print("Invalid input! Please enter 'e' for encryption or 'd' for decryption.")
