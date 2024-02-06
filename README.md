# Password Manager with Encryption

This Python script serves as a simple password manager with an added layer of security through encryption. The script utilizes the `cryptography` library and specifically the `Fernet` symmetric encryption scheme.

## Setup

Before running the password manager, you need to generate a secret key. This key will be used for encryption and decryption. Execute the following code to generate the key:

```python
from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open('secret_key.key', 'wb') as key_file:
        key_file.write(key)
        print("Key written to secret_key.key")

write_key()
```

**Note:** Ensure you run this code only once, and keep the generated key (`secret_key.key`) secure.

## Usage

1. Run the script and set your master password when prompted.
2. To add a new password, choose the "add" option and provide the username and password.
3. To view existing passwords, choose the "view" option.
4. To exit the password manager, enter "q" or "quit" when prompted.

## Security

The master password is encrypted and stored in the `master_password.txt` file. The passwords added to the manager are also encrypted using the Fernet key.

## Access Control

Access to the password manager is controlled by entering the correct master password at the beginning of the script. Ensure you remember this master password to access your stored passwords.

## Caution

Handle the `secret_key.key` file with care, as it is crucial for encrypting and decrypting passwords. Losing this key may result in permanent data loss.
