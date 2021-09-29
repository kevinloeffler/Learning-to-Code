"""
This package provides some useful counting operations for strings
"""

def characterCounter(string):
    count = 0

    for char in string:
        count += 1

    return count


def vocalCounter(string):
    count = 0
    vocals = ['a', 'e', 'i', 'o', 'u']

    for char in string:
        if char.lower() in vocals:
            count += 1

    return count
