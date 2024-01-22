while True:
    try:
        age = int(input())
        check_age(age)
    except ValueError:
        pass
    else:
        print(age)
        break