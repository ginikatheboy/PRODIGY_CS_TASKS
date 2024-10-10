import re

def assess_password_strength(password):
    # Define password criteria
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    number_criteria = bool(re.search(r'\d', password))
    special_char_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    
    
    # Initialize a strength counter
    strength = 0
    
    # Check each criterion and count how many are met
    if length_criteria:
        strength += 1
    if uppercase_criteria:
        strength += 1
    if lowercase_criteria:
        strength += 1
    if number_criteria:
        strength += 1
    if special_char_criteria:
        strength += 1

    # Determine password strength based on the number of criteria met
    if strength == 5:
        feedback = "Strong password!"
    elif 3 <= strength < 5:
        feedback = "Moderate password. Consider adding more complexity."
    else:
        feedback = "Weak password. Try adding uppercase letters, numbers, and special characters."

    return feedback

# Main program
password = input("Enter a password: ")
feedback = assess_password_strength(password)
print(feedback)
