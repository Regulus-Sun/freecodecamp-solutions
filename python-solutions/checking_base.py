def is_valid_number_og(n, base):
    values = "0123456789abcdefghijklmnopqrstuvwxyz"
    valid_digits = values[:base]

    for char in n.lower():
        if char not in valid_digits:
            return False
    return True

# Idiomatic and more optimized
def is_valid_number(n, base):
    if not (2 <= base <= 36):    # Validate the base
        return False

    values = "0123456789abcdefghijklmnopqrstuvwxyz"
    valid_digits = set(values[:base])    # Membership checks are faster with a set()

    return all(char.lower() in valid_chars for char in s)

# Python already knows how to parse numbers in bases up to 36. Some quirks with signed numbers and whitespace
def is_valid_number_built_in(s, base):
    try:
        int(s, base)
        return True
    except ValueError:
        return False


def is_valid_number_ord(s, base):
    if not (2 <= base <= 36):
        return False

    for char in s:
        if char.isdigit():
            value = ord(char) - ord('0')    # Converts character into integer
        elif char.isalpha():
            value = ord(char.lower()) - ord('a') + 10    # Converts character into its hexacimal notation
        else:
            return False    # invalid character
        
        if value >= base:
            return False

    return True
