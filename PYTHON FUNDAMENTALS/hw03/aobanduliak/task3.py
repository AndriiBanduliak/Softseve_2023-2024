# Replaces all occurrences of a character in a string with another character.

#   Args:
#     string: The string to replace characters in.
#     old_char: The character to replace.
#     new_char: The character to replace with.

#   Returns:
#     A string with all occurrences of `old_char` replaced with `new_char`.


def replace_all(string, old_char, new_char):

    new_string = ""
    for char in string:
        if char == old_char:
            new_string += new_char
        else:
            new_string += char

    return new_string


string = "Python is a better programming language. It is never too late to learn Python."

new_string = replace_all(string, "i", "&")

print(new_string)

