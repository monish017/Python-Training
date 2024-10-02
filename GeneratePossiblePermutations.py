from itertools import permutations

def generate_permutations(numbers):
    return list(permutations(numbers))

# Example Test Case
print(generate_permutations([1, 2, 3]))  
# Output: [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
