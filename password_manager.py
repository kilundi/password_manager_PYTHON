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

master_password=input("Enter your Master Password: ")
key=load_key() +  master_password.encode()
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