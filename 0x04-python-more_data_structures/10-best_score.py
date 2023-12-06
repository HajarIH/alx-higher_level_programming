#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    best = 0
    best_key = None
    for i, j in a_dictionary.items():
        if j > best:
            best = j
            best_key = i
    return best_key
