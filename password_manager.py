
from cryptography.fernet import  Fernet

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

def write_master_psw():
    master_password = input("Set your Master Password: ").lower()
    with open('master_password.txt', 'a') as f:
        f.write(f"{ferMaster.encrypt(master_password.encode()).decode()}\n")
# write_master_psw()
def  read_master_psw():
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

# print(master_password)

main_master_psw=input("Enter  the master password to proceed:").lower()

if  main_master_psw==master_password:
    print("\nAccess Granted\n")


    key=load_key() #+  master_password.encode()
    fer=Fernet(key)




    def add():
        username=input("Username: ")
        password=input("Password: ")

        with open('password.txt', 'a') as f:
            f.write(f"{username} : {fer.encrypt(password.encode()).decode()} \n".format())

    def view():
        with open('password.txt', 'r') as f:
            print("\n\nViewing Passwords:\n---------------------")
            for line in f:
                data=line.rstrip()
                user, passw=data.split(" : ")
                print(f"User: {user}, Password: {fer.decrypt(passw.encode()).decode()}")
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
    print("\nWrong Password!\n")
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
