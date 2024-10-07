# PRODIGY_CS_01: Caesar Cipher - Encryption & Decryption

### Overview
This is the first task of the **PRODIGY_CS** series, where a Python program is used to perform **Caesar Cipher** encryption and decryption. The Caesar Cipher shifts each letter of the input text by a specified number of positions in the alphabet.

### How It Works
- **Encryption**: Shifts each letter in the message forward by the provided shift value.
- **Decryption**: Reverses the shift to return the encrypted message to its original form.

### Usage
1. **Run the Program**:
   ```bash
   python Task01.py
   ```
2. **Input**:
   - Message to encrypt or decrypt.
   - Shift value (an integer) for the cipher.

3. **Example**:
   - **Message**: `hello`
   - **Shift**: `3`
   - **Encrypted Message**: `khoor`
   - **Decrypted Message**: `hello`




# PRODIGY_CS_02: Image Encryption and Decryption Tool

## Overview
This project is the second task completed during my internship at ProdigyInfotech. It implements a simple image encryption and decryption tool using pixel manipulation. The program allows users to encrypt or decrypt images using a basic XOR operation on pixel values.

## Features
- User-friendly interface for choosing between encryption and decryption.
- Encrypts images using a key to manipulate pixel values.
- Decrypts images back to their original form using the same key.
- Outputs encrypted and decrypted images as new files.

## Technologies Used
- Python
- No external libraries required (uses built-in file handling)

## Code Explanation
The main functionality of the program is based on manipulating pixel values of images through the XOR operation. Below is an overview of the provided code:

### Code Snippet
```python
# Encrypt or Decrypt an image using a simple XOR operation.

file = open('image.jpg', "rb")  # Open the image file in binary read mode
image = file.read()  # Read the content of the image
file.close()  # Close the file

image = bytearray(image)  # Convert the image content to a bytearray for manipulation
key = 48  # Define a simple key for encryption/decryption

# Perform the XOR operation on each pixel value
for i, j in enumerate(image):
    image[i] = j ^ key  # XOR each pixel value with the key

# Code to save the encrypted image as a new file
file = open("encrypted.jpg", "wb")  # Open a new file in binary write mode
file.write(image)  # Write the manipulated image content to the file
file.close()  # Close the file
```

## Usage
1. **Run the program**: Open your terminal or command prompt and execute the following command:
   ```bash
   python Task02.py
   ```

2. **Choose an option**: When prompted, enter `e` to encrypt an image or `d` to decrypt an image.

3. **Provide file paths**:
   - For encryption:
     ```bash
     Enter the path of the image to encrypt: input_image.jpg
     Enter the name for the encrypted image: encrypted_image.jpg
     ```

   - For decryption:
     ```bash
     Enter the path of the image to decrypt: encrypted_image.jpg
     Enter the name for the decrypted image: decrypted_image.jpg
     ```

## Example
To encrypt an image:
```plaintext
Choose an option: e
Enter the path of the image to encrypt: input_image.jpg
Enter the name for the encrypted image: encrypted_image.jpg
```

To decrypt an image:
```plaintext
Choose an option: d
Enter the path of the image to decrypt: encrypted_image.jpg
Enter the name for the decrypted image: decrypted_image.jpg
```

## Contributing
Feel free to fork this repository and submit pull requests with improvements or enhancements.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
