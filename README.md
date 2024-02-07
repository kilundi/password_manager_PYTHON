# Password Manager Readme

## Introduction

This Python script serves as a basic password manager that focuses on security through encryption using the Fernet module from the cryptography library. The manager allows users to store and retrieve passwords securely.

## Features

1. **Key Generation:**

   - The script generates a secret key and saves it to a file (`secret_key.key`) to ensure secure encryption and decryption processes.

2. **Security Question:**

   - Users can set a security question and answer during the initial setup to enhance the security of the master password.

3. **Master Password:**

   - The script encrypts and stores the master password in a file (`master_password.txt`). It also prompts the user to enter the master password to access stored passwords.

4. **Password Storage:**

   - Users can add new passwords, associating them with usernames. Passwords are stored in an encrypted form in the `password.txt` file.

5. **Viewing Passwords:**

   - Users can view their stored passwords in a decrypted form, providing an option to either add new passwords or view existing ones.

6. **Reset Master Password:**
   - In case the user forgets the master password, there is a reset option involving answering the security question before setting a new master password.

## Usage

1. **Initialization:**

   - Run the script to initialize the password manager.
   - The script will prompt you to set a security question and answer during the first run.

2. **Access:**

   - Enter the master password to gain access to the password manager.

3. **Operations:**

   - Choose between adding new passwords, viewing existing ones, or quitting the manager.

4. **Security Measures:**
   - The script employs encryption and decryption techniques to ensure the security of sensitive information.

## File Structure

- **secret_key.key:** Contains the secret key generated for encryption.
- **security_questions.txt:** Stores the encrypted security question.
- **master_password.txt:** Stores the encrypted master password.
- **password.txt:** Contains encrypted usernames and passwords.

## Important Notes

- It is crucial to remember the master password, as it is used to access all stored passwords.
- Ensure the security of the key and password files, and consider using a secure location to store them.

## Dependencies

- [cryptography](https://cryptography.io/): The script utilizes the Fernet module from this library for encryption and decryption processes.

## Disclaimer

This script provides basic password management functionality and should be used with caution. Ensure the security of your files and consider additional measures for protecting sensitive information.

## Contribution

Feel free to contribute to the improvement of this password manager. Report any issues or suggest enhancements through the repository.

---

**STARNSLAUS KILUNDI**
_23 years old_
_Student pursuing a career in IT, focusing on Frontend Development_
_Based in Kenya_
_Aspiring Frontend Developer and Forex Trader_
