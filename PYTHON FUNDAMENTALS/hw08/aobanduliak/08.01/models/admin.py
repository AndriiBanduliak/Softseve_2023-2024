from models.user import User

class Admin(User):
    def __init__(self, name):
        super().__init__(name)

def create_admin(name):
    admin = Admin(name)
    print(f"Admin {admin.name} created!")
    return admin
