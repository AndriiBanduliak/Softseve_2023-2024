def day_of_week():
    try:
        day = int(input("Enter a number: "))
        if day < 1 or day > 7:
            raise ValueError("Invalid number. Enter a number between 1 and 7.")
        days = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}
        print(f"The day of the week is {days[day]}.")
    except ValueError as e:
        print(e)

day_of_week()
