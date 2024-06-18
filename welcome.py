class User:
    def __init__(self, name, surname, email):
        self.name = name
        self.surname = surname
        self.email = email

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Hey User type in your name:")
    print_hi(input())

try:
    user = open("user.txt", 'r')
except:
    print("User file not exist. Creating new file.")
    user = open("user.txt", 'x')


