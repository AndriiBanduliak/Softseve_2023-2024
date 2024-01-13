class User:
    def __init__(self, name):
        self.name = name

def create_user(name):
    user = User(name)
    print(f"User {user.name} created!")
    return user
