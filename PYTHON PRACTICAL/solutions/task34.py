import json
import csv

# Custom exceptions


class DepartmentName(Exception):
    pass


class InvalidInstanceError(Exception):
    pass

# Function to validate the user JSON format


def validate_user_json(data):
    if not isinstance(data, list):
        raise InvalidInstanceError("User data should be a list of objects.")

    for user in data:
        if not isinstance(user, dict):
            raise InvalidInstanceError("Each user entry must be an object.")
        if not all(key in user for key in ["id", "name", "department_id"]):
            raise InvalidInstanceError("Error in user schema")
        if not isinstance(user['id'], int) or not isinstance(user['name'], str) or not isinstance(user['department_id'], int):
            raise InvalidInstanceError("Invalid types for user fields.")

# Function to validate the department JSON format


def validate_department_json(data):
    if not isinstance(data, list):
        raise InvalidInstanceError(
            "Department data should be a list of objects.")

    for dept in data:
        if not isinstance(dept, dict):
            raise InvalidInstanceError(
                "Each department entry must be an object.")
        if not all(key in dept for key in ["id", "name"]):
            raise InvalidInstanceError("Error in department schema")
        if not isinstance(dept['id'], int) or not isinstance(dept['name'], str):
            raise InvalidInstanceError("Invalid types for department fields.")

# Function to create CSV file with user and department information


def user_with_department(csv_file, user_json, department_json):
    # Load user and department data from JSON files
    with open(user_json, 'r') as user_file, open(department_json, 'r') as dept_file:
        users = json.load(user_file)
        departments = json.load(dept_file)

    # Validate the users and departments manually
    validate_user_json(users)
    validate_department_json(departments)

    # Create a dictionary for quick department lookup
    dept_dict = {dept['id']: dept['name'] for dept in departments}

    # Open the CSV file for writing
    with open(csv_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # Write header
        writer.writerow(['name', 'department'])

        # Write user information along with corresponding department
        for user in users:
            dept_id = user['department_id']
            user_name = user['name']

            # Check if the department exists
            if dept_id not in dept_dict:
                raise DepartmentName(f"Department with id {
                                     dept_id} doesn't exists")

            # Write user name and department name to CSV
            writer.writerow([user_name, dept_dict[dept_id]])

# Example usage:
# user_with_department('output.csv', 'user.json', 'department.json')
