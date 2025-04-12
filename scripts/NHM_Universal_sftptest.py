# © 2025 Nathanael Hernandez – Universal version
# This script has been sanitized to remove any proprietary or sensitive information.

#Author: Nathanael Hernandez
#Date: 2023-10-04
#Version: 1.0
#Description: This script is used to test the connection to a remote server using SFTP with a private key and access_token.
# It uses the paramiko library to establish the connection and handle any exceptions that may occur.

import paramiko
import base64

hostname = ''
port = 22
username = ''

private_key_path = ""
access_token = ''

client = paramiko.SSHClient()
client.load_system_host_keys()


client.set_missing_host_key_policy(paramiko.AutoAddPolicy())


try:
    private_key = paramiko.RSAKey(filename=private_key_path,credential=access_token)

    client.connect(hostname,port,username,pkey=private_key)

    sftp = client.open_sftp()
except Exception as e:
    print(f'error {e}')
finally:
    sftp.close()
    client.close()
