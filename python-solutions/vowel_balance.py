def is_balanced_og(s):
    # Use set for faster lookup
    vowels = set("aeiouAEIOU")
    mid = len(s)//2
    
    first = s[:mid]

    # If string is odd
    if len(s) % 2 == 0:
        second = s[mid:]
    else:
        second = s[mid+1:]

    count1 = 0
    count2 = 0
    
    for c in first:
        if c in vowels:
            count1 += 1

    for c in second:
        if c in vowels:
            count2 += 1
            
    return count1 == count2

# Cleaner version using sum()
def is_balanced(s):
    vowels = "aeiouAEIOU"
    mid = len(s) // 2
    
    first_half = s[:mid]
    second_half = s[mid:] if len(s) % 2 == 0 else s[mid+1:]

    count1 = sum(1 for char in first_half if char in vowels)
    count2 = sum(1 for char in second_half if char in vowels)
    
    return count1 == count2
