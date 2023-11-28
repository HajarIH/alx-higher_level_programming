#!/usr/bin/python3
def print_last_digit(number):
    modulo = abs(number) % 10
    print(modulo, end="")
    return modulo
