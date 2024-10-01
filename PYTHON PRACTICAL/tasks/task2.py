def morse_digit(digit):
    # Define the Morse code for the digits using the pattern described
    if digit == '1':
        return '.----'
    elif digit == '2':
        return '..---'
    elif digit == '3':
        return '...--'
    elif digit == '4':
        return '....-'
    elif digit == '5':
        return '.....'
    elif digit == '6':
        return '-....'
    elif digit == '7':
        return '--...'
    elif digit == '8':
        return '---..'
    elif digit == '9':
        return '----.'
    elif digit == '0':
        return '-----'


def morse_number(number):
    # Convert each digit to its Morse code equivalent
    return ' '.join(morse_digit(digit) for digit in number)
