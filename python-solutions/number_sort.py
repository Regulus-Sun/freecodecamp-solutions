def sort_numbers_og(s):
    numbers = []
    list_of_num = s.split(",")

    for n in list_of_num:
        try:
            numbers.append(int(n))
        except:
            continue

    return sorted(numbers)

# concise and improved
def sort_numbers(s):
    result = []
    for n in s.split(","):
        try:
            result.append(int(n))
        except ValueError: # It's better to catch only the specific exception you're expecting.
            pass           # It avoids accidentally hiding other bugs that a bare except: would catch.
    return sorted(result)

# Idiomatic AI
def sort_numbers_iai(s):
    return sorted(int(x) for x in s.split(','))
