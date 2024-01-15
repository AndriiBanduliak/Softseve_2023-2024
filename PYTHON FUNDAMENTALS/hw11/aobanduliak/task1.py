def process_age():
    try:
        age = int(input("Enter your age: "))
        if age < 0:
            raise ValueError("Age cannot be negative.")
        elif age % 2 == 0:
            print("Your age is even.")
        else:
            print("Your age is odd.")
    except ValueError as e:
        print(e)

process_age()
