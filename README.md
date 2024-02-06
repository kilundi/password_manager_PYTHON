---

# Password Manager

This is a basic password manager script written in Python, utilizing the `cryptography` library's `Fernet` for encryption.

## Features:

1. **Key Generation:**
    - The script generates a secret key using `Fernet.generate_key()` and stores it in a file named `secret_key.key`.

2. **Adding Passwords:**
    - Users can add new passwords by providing a username and password. The passwords are encrypted using the generated key and stored in a file named `password.txt`.

3. **Viewing Passwords:**
    - Users can view existing passwords. The stored passwords are decrypted using the generated key and displayed in a readable format.

## How to Use:

1. **Key Generation:**
    - The script automatically generates a secret key and writes it to `secret_key.key` the first time it is run.

2. **Adding Passwords:**
    - Run the script and choose the option to add a new password.
    - Enter the username and password when prompted.

3. **Viewing Passwords:**
    - Run the script and choose the option to view existing passwords.
    - Enter the master password when prompted.

4. **Quitting:**
    - To exit the script, choose the option to quit by entering 'q' or 'quit'.

## Security Note:

- The master password provided during the script execution is used to enhance the security of the stored passwords. Make sure to remember your master password as it is crucial for decrypting passwords.

---
