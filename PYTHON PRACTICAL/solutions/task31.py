class ToSmallNumberGroupError(Exception):
    pass


def check_number_group(number):
    try:
        number = int(number)
        if number <= 10:
            raise ToSmallNumberGroupError(
                "Number of your group can't be less than 10")
        else:
            return f"Number of your group {number} is valid"
    except ValueError:
        return "You entered incorrect data. Please try again."
    except ToSmallNumberGroupError as e:
        return f"We obtain error:{e}"
