
correct_login = "First"

user_login = ""

while True:

    user_login = input("Enter login: ")

    if user_login == correct_login:

        print("Hello, " + user_login + "!")
        break
    else:

        print("Try again")
