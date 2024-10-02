def second_largest(numbers):
    unique_numbers = list(set(numbers))  # Remove duplicates
    unique_numbers.sort()
    return unique_numbers[-2]  # Second last element

# Example Test Case
print(second_largest([10, 20, 4, 45, 99]))  # Output: 45
