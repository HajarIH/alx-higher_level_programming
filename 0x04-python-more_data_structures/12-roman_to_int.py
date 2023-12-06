def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    total = 0
    x = 0
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in reversed(roman_string):
        x = roman[i]
        total += x if total < x * 5 else -x
    return total
