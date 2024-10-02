from itertools import combinations

def find_combinations(tuple_data, target):
    result = []
    for r in range(1, len(tuple_data) + 1):
        for combo in combinations(tuple_data, r):
            if sum(combo) == target:
                result.append(combo)
    return result

# Example Test Case
print(find_combinations((2, 3, 5, 7), 10))  # Output: [(3, 7), (2, 3, 5)]
