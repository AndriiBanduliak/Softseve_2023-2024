def day_of_week(day):
    try:
        day = int(day)
        if 1 <= day <= 7:
            days = ["Monday", "Tuesday", "Wednesday",
                    "Thursday", "Friday", "Saturday", "Sunday"]
            return days[day - 1]
        else:
            return "There is no such day of the week! Please try again."
    except ValueError:
        return "You did not enter a number! Please try again."
