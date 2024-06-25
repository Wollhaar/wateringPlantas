import json


class User:
    def __init__(self, name, surname, email):
        self.name = name
        self.surname = surname
        self.email = email

    def __str__(self):
        return f'{"name":{self.name}, "surname": {self.surname}, "email": {self.email}}'

    @classmethod
    def new_user(cls):
        # taking new user data by user input
        print("Hey User type in your name:")
        name = input()
        print("Type your surname (optional)")
        surname = input()
        print("Type your email")
        email = input()
        return name, surname, email

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.

def create_user(mode):
    # Use a breakpoint in the code line below to debug your script.
    name, surname, email = User.new_user()
    user = User(name, surname, email)
    file = open("user.json", mode)
    file.write(json.dumps(user)) #TODO: make user serializable to json
    return user

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    try:
        file = open("user.json", 'r')
        user = file.read()
        if len(user) == 0:
            raise ValueError("User not set")

    except FileNotFoundError:
        print("User file not exist. \nCreating new file. \nCreating new User.")
        user = create_user('x')

    except ValueError:
        print("User file exist, but empty. \nOverwriting file. \nCreating new User.")
        user = create_user('w')


    print_hi(user)



