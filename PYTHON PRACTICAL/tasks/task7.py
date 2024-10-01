def outer(name):
    def inner():
        print(f"Hello, {name}!")
    return inner