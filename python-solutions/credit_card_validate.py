def is_valid_card_og(number):
    total = 0
    double_digit = False

    for digit in reversed(number):
        n = int(digit)

        if double_digit:
            n *= 2
            if n > 9:
                n -= 9
        total += n

        double_digit = not double_digit
    
    return total % 10 == 0

# More explicit tracking though index
def is_valid_card(number):
    total = 0

    for i, digit in enumerate(reversed(number)):
        n = int(digit)

        if i % 2:
            n = n * 2 - 9 if n > 4 else n * 2 # A small optimization because any digit 5–9 doubled will exceed 9.

        total += n

    return total % 10 == 0

def is_valid_card_iai(number):
    total = sum(
        (d * 2 - 9 if d > 4 else d * 2) if i % 2 else d
        for i, d in enumerate(map(int, reversed(number)))
    )
    return total % 10 == 0
