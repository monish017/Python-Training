def longest_word(sentence):
    words = sentence.split()
    longest = max(words, key=len)
    return longest

# Example Test Case
print(longest_word("The quick brown fox jumps over the lazy dog"))  # Output: "jumps"
