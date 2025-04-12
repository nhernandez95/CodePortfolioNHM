# © 2025 Nathanael Hernandez – Universal version
# This script has been sanitized to remove any proprietary or sensitive information.

#Author: Nathanael H.
# Date: 2025-03-01
# Purpose: This script demonstrates how to encrypt and decrypt credentials using the cryptography library in Python.
# Description: This script demonstrates how to encrypt and decrypt credentials using the cryptography library in Python.
# It generates a key, encrypts the username and credential, and then decrypts them back to their original form.
# Ensure you have the cryptography library installed in your Python environment. You can install it using pip:
# pip install cryptography
# Import necessary libraries
from cryptography.fernet import Fernet

# Generate a key and instantiate a Fernet instance
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Your credentials
username = "your_username"
credential = "your_credential"

# Encrypt the credentials
encrypted_username = cipher_suite.encrypt(username.encode())
encrypted_credential = cipher_suite.encrypt(credential.encode())

print(f"Encrypted Username: {encrypted_username}")
print(f"Encrypted credential: {encrypted_credential}")

# Decrypt the credentials
decrypted_username = cipher_suite.decrypt(encrypted_username).decode()
decrypted_credential = cipher_suite.decrypt(encrypted_credential).decode()

print(f"Decrypted Username: {decrypted_username}")
print(f"Decrypted credential: {decrypted_credential}")