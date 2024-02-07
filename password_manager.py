
from cryptography.fernet import  Fernet
import os

'''
def write_key():
    key = Fernet.generate_key()
    with open('secret_key.key', 'wb') as key_file:
        key_file.write(key)
        print ("Key written to secret_key.key")

write_key()
'''




def load_key():
    file=open('secret_key.key','rb')
    key=file.read()
    return key

master=load_key()
ferMaster=Fernet(master)

def security_question():
    print("\n")
    print("Please set a security question")
    print("\n")
    security_questions = input("What's your pet: ").lower()
    with open('security_questions.txt', 'w') as f:
        f.write(f"{ferMaster.encrypt(security_questions.encode()).decode()}\n")
    print("Security question set successfully")
    print("\n")

def read_security_question():
    file_path ='security_questions.txt'
    if not os.path.exists(file_path):
        print("\n")
        print(f"'{file_path}' is not available.")
        print("\n")
        security_question()

    else:
        with open('security_questions.txt', 'r') as f:
            if f.read().strip()=="":
                print("\n")
                print("Security question's not set: ")
                security_question()
            else:
                f.seek(0)
                for line in f:
                    security_answer=ferMaster.decrypt(line.encode()).decode()
                    return security_answer

def compare_security_answer():
    answer=input("Whats your pet: ").lower()
    if answer==read_security_question():
        write_master_psw()
    else:
        print("\n")
        print(f"Sorry {answer} doesn't match the expected answer.")
        quit()

def write_master_psw():
    master_password = input("Set your Master Password: ").lower()
    with open('master_password.txt', 'w') as f:
        f.write(f"{ferMaster.encrypt(master_password.encode()).decode()}\n")
    print("\n")
    print("Master password set successfully")

    read_security_question()

def  read_master_psw():
     file_path='master_password.txt'
     if not os.path.isfile(file_path):
         write_master_psw()
     else:
        with open('master_password.txt', 'r') as f:
            if f.read().strip() =="":
                print("Master password is not set")
                write_master_psw()


            else:
                f.seek(0)
                for line in f:
                    password=ferMaster.decrypt(line.strip().encode()).decode()
                return password


master_password=read_master_psw()

main_master_psw=input("Enter  the master password to proceed: ").lower()

if  main_master_psw==master_password:
    print("\nAccess Granted\n")


    key=load_key()
    fer=Fernet(key)




    def add():
        username=input("Username: ")
        password=input("Password: ")

        with open('password.txt', 'a') as f:
            f.write(f"{username} : {fer.encrypt(password.encode()).decode()} \n".format())

    def view():
        file_path ='password.txt'
        if not os.path.exists(file_path):
            print(f"'{file_path}' is not available.")
            add()
        else:
            with open('password.txt', 'r') as f:
                if f.read().strip( ) == '':
                    print("File is empty.\nAdd a record first.")
                    add()
                else:
                    print("\n\nViewing Passwords:\n---------------------")
                    f.seek(0)
                    for line in f:
                        data=line.rstrip()
                        user, passw=data.split(" : ")
                        print(f"User: {user}, Password: {fer.decrypt(passw.encode()).decode()} \n")
                    print("\n")
    while True:
        mode=input("Would you want to add new password or view existing ones (view or add or q or quit): ").lower()

        if mode =="q" or mode=="quit":
            break
        if mode == "add":
            add()
        elif mode=="view":

            view()
        else:
            print(f"Invalid option {mode}!")
            continue

else:
    print("\n")
    print("\nWrong Password!\n")
    print("\n")
    reset_psw=input("Do you want to Reset the Master Password? (y/N): ").lower()
    if reset_psw=='y':
        compare_security_answer()
    elif  reset_psw == 'n':
        exit()





# from cryptography.fernet import Fernet

# def write_key():
#     key = Fernet.generate_key()
#     with open('secret_key.key', 'wb') as key_file:
#         key_file.write(key)
#         print("Key written to secret_key.key")

# # Uncomment the next line to generate and write the key only once
# # write_key()


# def load_key():
#     with open('secret_key.key', 'rb') as key_file:
#         key = key_file.read()
#     return key

# def get_master_password():
#     while True:
#         password = input("Enter your master password: ").lower()
#         if password =='kilundi':
#             return password
#         else:
#             print("Incorrect password, please try again.")
#             continue

# def derive_key(master_password):
#     key = load_key() + master_password.encode()
#     return key

# def initialize_fernet(master_password):
#     key = derive_key(master_password)
#     return Fernet(key)

# def add(fer):
#     username = input("Username: ")
#     password = input("Password: ")

#     with open('password.txt', 'a') as f:
#         encrypted_password = fer.encrypt(password.encode()).decode()
#         f.write(f"{username} : {encrypted_password}\n")

# def view(fer):
#     with open('password.txt', 'r') as f:
#         print("\n\nViewing Passwords:\n---------------------")
#         for line in f:
#             data = line.rstrip()
#             user, passw = data.split(" : ")
#             decrypted_password = fer.decrypt(passw.encode()).decode()
#             print(f"User: {user}, Password: {decrypted_password}")

# # Main program
# while True:
#     master_password = get_master_password()
#     fer = initialize_fernet(master_password)

#     mode = input("Would you want to add a new password or view existing ones (add, view, q or quit): ").lower()

#     if mode == "q" or mode == "quit":
#         break
#     elif mode == "add":
#         add(fer)
#     elif mode == "view":
#         view(fer)
#     else:
#         print(f"Invalid option {mode}!")
#         continue
