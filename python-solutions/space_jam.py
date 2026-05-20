def space_jam_og(s):
    string = "".join(s.split())
    return "  ".join(list(string.upper()))


def space_jam(s):
    return "  ".join("".join(s.split()).upper())


def space_jam_exp(s):
    # Remove all spaces
    no_spaces = "".join(s.split())

    # Convert to uppercase
    uppercase_text = no_spaces.upper()

    # Add two spaces between each character
    return "  ".join(uppercase_text)
