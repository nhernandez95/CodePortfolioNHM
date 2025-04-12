# © 2025 Nathanael Hernandez – Universal version
# This script has been sanitized to remove any proprietary or sensitive information.

import random
import string

# Define the character sets
lower = string.ascii_lowercase
upper = string.ascii_uppercase
digits = string.digits
symbols = "!@#$%^&*()-_=+[]{}|;:,.<>?/"

# Ensure the credential has at least one character from each set
credential = [
    random.choice(lower),
    random.choice(upper),
    random.choice(digits),
    random.choice(symbols)
]

# Remove the chosen characters from their respective sets to ensure uniqueness
lower = lower.replace(credential[0], '')
upper = upper.replace(credential[1], '')
digits = digits.replace(credential[2], '')
symbols = symbols.replace(credential[3], '')

# Fill the rest of the credential length with a mix of all character sets ensuring uniqueness
all_characters = lower + upper + digits + symbols
credential += random.sample(all_characters, k=12-4)

# Shuffle the credential list to ensure randomness
random.shuffle(credential)

# Convert the list to a string and print it
print(''.join(credential))