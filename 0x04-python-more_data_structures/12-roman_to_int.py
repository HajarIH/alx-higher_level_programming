def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    total = 0
    x = 0
    for i in reversed(roman_string):
        x = roman_string[i]
        total += x if total < x * 5 else -x
    return total
