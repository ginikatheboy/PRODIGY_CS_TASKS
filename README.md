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




# PRODIGY_CS_03: Password Strength Assessment Tool

## Project Overview

This tool assesses the strength of a password based on several criteria such as length, the presence of uppercase and lowercase letters, numbers, and special characters. It provides feedback to users on the strength of their password, categorizing it as **Weak**, **Moderate**, or **Strong**.

This is the **PRODIGY_CS_03** task from my internship at ProdigyInfotech, where I am learning about cybersecurity and hands-on coding.

## Features

- **Password Length Check:** Validates that the password is at least 8 characters long.
- **Character Variety:** Checks for the presence of uppercase letters, lowercase letters, numbers, and special characters.
- **Password Strength Classification:**
  - **Weak**: If the password has fewer than 8 characters or lacks variety.
  - **Moderate**: If the password has a combination of letters and numbers.
  - **Strong**: If the password meets all the criteria with a good balance of characters.

## Usage

1. **Clone the repository**:
   ```bash
   git clone https://github.com/ginikatheboy/PRODIGY_CS_TASKS.git
   ```

2. **Navigate to the project folder**:
   ```bash
   cd PRODIGY_CS_TASKS/PRODIGY_CS_03
   ```

3. **Run the Python script**:
   ```bash
   python password_strength_checker.py
   ```

4. **Input your password** when prompted to see its strength evaluation.

## Code Explanation

The Python script evaluates a password based on:
- **Length**: Ensures the password has at least 8 characters.
- **Uppercase and Lowercase Letters**: Checks if the password includes both upper and lower case letters.
- **Numbers**: Validates the presence of at least one number.
- **Special Characters**: Looks for any non-alphanumeric characters.

The tool then provides feedback depending on how many of these criteria are met.

## Example

```bash
Enter a password: Password123!
Your password is strong.
```

## Future Improvements

- Adding suggestions for improving weak passwords.
- Implementing a graphical user interface (GUI) for better usability.





# PRODIGY_CS_04: Simple Keylogger

This project is a simple keylogger built using Python and the `pynput` library. The keylogger records each keystroke made by the user and saves them to a log file (`keyfile.txt`). It is created as part of an internship task with **Prodigy Infotech**.

> **Note:** This project is for educational purposes only. Ethical considerations and permissions are crucial when working on keyloggers or similar programs.

## Features

- Logs all key presses (including special keys like `Enter`, `Space`, and `Shift`).
- Saves the keystrokes to a log file (`keyfile.txt`) in the same directory.
- Designed to run in the background and capture keystrokes without interfering with other programs.

## Getting Started

### Prerequisites

Before running the keylogger, ensure that you have Python installed on your system. You also need to install the `pynput` library.

To install `pynput`, run the following command:

```bash
pip install pynput
```

### Running the Keylogger

1. Clone this repository to your local machine or download the code.
   
2. Run the script using Python:

```bash
python keylogger.py
```

3. The keylogger will run in the background, and every keystroke will be logged in the `keyfile.txt` file.

### Example Log Output

When typing on the keyboard, the log file will record regular and special keys as follows:

```
a
b
c
<Key.space>
<Key.enter>
1
2
3
```

## Ethical Considerations

Keyloggers can potentially be used to capture sensitive information such as passwords or private communications. It is important to only use this tool in a legal and ethical manner. Ensure you have the necessary permissions to log keystrokes on any system where you use this tool.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- **Prodigy Infotech** for the internship opportunity and task.
- **pynput** library for providing easy control of input devices in Python.
