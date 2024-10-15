def run_calc(a, b, op):
    try:
        if op == 0:
            print(a + b)
        elif op == 1:
            print(a - b)
        elif op == 2:
            print(a * b)
        elif op == 3:
            print(a / b)
        else:
            raise ValueError
    except ValueError:
        print("Incorrect operation is obtained")
    except TypeError:
        print("TypeError")
    except NameError:
        print("NameError")
    except ZeroDivisionError:
        print("Division by zero")
    except:
        print("Error")
    finally:
        print('End of calculation')
