import json
import logging
import os

# Set up logging configuration
logging.basicConfig(filename='app.log', filemode='w',
                    format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.ERROR)


def parse_user(output_file, *input_files):
    users_dict = {}

    for file in input_files:
        try:
            # Check if file exists
            if not os.path.exists(file):
                logging.error(f"File {file} doesn't exist")
                continue

            # Load user data from the file
            with open(file, 'r') as f:
                users = json.load(f)

            # Update the dictionary with user data, unique by 'name'
            for user in users:
                name = user['name']
                if name in users_dict:
                    # Merge user info if name already exists
                    users_dict[name].update(user)
                else:
                    users_dict[name] = user

        except json.JSONDecodeError:
            logging.error(f"Error decoding JSON from file {file}")
        except Exception as e:
            logging.error(
                f"An error occurred while processing file {file}: {e}")

    # Write the merged users' data to the output file
    with open(output_file, 'w') as f:
        json.dump(list(users_dict.values()), f, indent=4)

# Example usage:
# parse_user('user3.json', 'user1.json', 'user2.json')
