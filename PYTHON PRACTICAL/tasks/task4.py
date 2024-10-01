import re


def pretty_message(text):
    """Removes duplicated groups of characters within words.

    Args:
        text: The input text.

    Returns:
        The text with duplicated groups of characters removed.
    """
    # Pattern to match any repeating group of two or more characters
    pattern = r'(\w+?)\1+'
    return re.sub(pattern, r'\1', text)
