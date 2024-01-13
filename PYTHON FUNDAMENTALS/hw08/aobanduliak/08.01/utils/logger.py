import datetime

def log_in_file(message, file_path="log.txt"):
    with open(file_path, "a") as file:
        file.write(f"{datetime.datetime.now()}: {message}\n")
    print(f"Logged message in {file_path}!")
