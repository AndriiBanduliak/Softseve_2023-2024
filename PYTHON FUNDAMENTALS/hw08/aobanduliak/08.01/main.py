from models.user import create_user
from models.admin import create_admin
from utils.logger import log_in_file
from utils.formatter import format_string

print(list(filter(lambda s: not ("_" in s), dir())))

# Call the functions
user = create_user("John Doe")
admin = create_admin("Jane Doe")
log_in_file("This is a log message.")
formatted_string = format_string("This is a string to format.", "lower")

print(f"Formatted string: {formatted_string}")
