import re

def check(login):
    # Convert the login to lowercase to make the check case-insensitive
    login_lower = login.lower()

    try:
        # Split the login into role and id using various separators
        separators = ['-id', '-']
        role, id_part = None, None

        for separator in separators:
            parts = login_lower.split(separator, 1)
            if len(parts) == 2:
                role, id_part = parts
                break

        # If separator not found, try 'id'
        if role is None or id_part is None:
            parts = login_lower.split('id', 1)
            if len(parts) == 2 and parts[1] != '':
                role, id_part = parts

        if role is None or id_part is None or not id_part.isdigit():
            raise ValueError(f"incorrect login '{login}'")

        id_number = int(id_part)

        # Check if the role is 'admin' or 'employee'
        if role not in ['admin', 'employee']:
            raise ValueError(f"incorrect login '{login}'")

        # Everything is correct, return True
        return True
    except ValueError:
        # Re-raise the ValueError without additional information
        raise
