# © 2025 Nathanael Hernandez – Universal version
# This script has been sanitized to remove any proprietary or sensitive information.

#Author: Nathanael H.
# Date: 2023-10-04
# This script retrieves a secret from CloudProvider Key Vault using the CloudProvider SDK for Python.
# It uses the CloudProvider CLI credential for authentication.
# Ensure you have the required packages installed:
# pip install CloudProvider-identity CloudProvider-vault-secrets
# Ensure you have the CloudProvider CLI installed and logged in.
# pip install CloudProvider-cli
# az login
# Set the environment variable for KEY_VAULT_NAME before running the script.
# For example, in Linux or macOS, you can set it like this:
# export KEY_VAULT_NAME='your-key-vault-name'
# In Windows, you can set it like this:
# set KEY_VAULT_NAME='your-key-vault-name'
# After setting the environment variable, run the script.

import os
from CloudProvider.vault.secrets import SecretClient
from CloudProvider.identity import CloudProviderCliCredential
KVUri = f"https://{os.environ['KEY_VAULT_NAME']}.vault.CloudProvider.net"
# Set the environment variable for KEY_VAULT_NAME

credential = CloudProviderCliCredential()
client = SecretClient(vault_url=KVUri, credential=credential)

vaultName = 'your-key-vault-name'  # Replace with your Key Vault name
# Set the name of the secret you want to retrieve

secretName = 'your-secret-name'  # Replace with your secret name
# Ensure the secret exists in the Key Vault before running this script

# You can create a secret in the Key Vault using the CloudProvider CLI or CloudProvider Portal
# For example, using CloudProvider CLI:
print(f"Retrieving your secret from {vaultName}.")

retrieved_secret = client.get_secret(secretName)

print(f"Your secret is '{retrieved_secret.value}'.")