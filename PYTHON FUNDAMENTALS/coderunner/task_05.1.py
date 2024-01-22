def binary(decimal):
    if decimal == 0:
        return "0"
    
    binary_str = ""
    while decimal > 0:
        binary_str = str(decimal % 2) + binary_str
        decimal = decimal // 2

    return binary_str