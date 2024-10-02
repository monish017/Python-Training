def invert_dictionary(dictionary):
    return {v: k for k, v in dictionary.items()}

# Example Test Case
print(invert_dictionary({'a': 1, 'b': 2, 'c': 3}))  # Output: {1: 'a', 2: 'b', 3: 'c'}
