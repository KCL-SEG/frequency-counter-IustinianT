"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    while len(items) > 0:
        current_item = items.pop(0)
        if current_item not in frequencies:
            frequencies[current_item] = 1
        else:
            frequencies[current_item] += 1

    return frequencies