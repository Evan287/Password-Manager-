from cryptography.fernet import fernet

master_pwd = input("What is the master password") # User inputs their master password

def view():  # View function
    with open('passwords.txt', 'r' ) as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|") # Assigns first element to user and second element to passw
            "Hello|Evan"
            ["Hello", "Tim"]
            print("User:", user, ", Password:", passw)


def add(): # Add function to add a password
    name = input("Account name: ")
    pwd = input("Password: ")

    with open('passwords.txt', 'a' ) as f: # modes are w,r, a w is write mode, r is read mode, a is append mode add
        f.write(name + "|" +pwd + "\n")  # takes name, separates pwd with pipe operator then takes the password
while True:
    mode = input("Would you like to add a new password or view existing ones(view, add), press q to quit ?")                              # allows user input
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode")
        continue