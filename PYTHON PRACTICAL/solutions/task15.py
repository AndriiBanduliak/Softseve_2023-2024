class Employee:
    def __init__(self, full_name, **kwargs):
        self.name, self.lastname = full_name.split()
        for key, value in kwargs.items():
            setattr(self, key, value)
