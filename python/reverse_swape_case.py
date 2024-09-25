import re

def check_space_and_non_english(sentence):
    # Check if the sentence contains spaces
    contains_space = any(char.isspace() for char in sentence)
    
    # Check if the sentence contains non-English letters
    contains_non_english = bool(re.search(r'[^a-zA-Z\s]', sentence))
    
    return contains_space, contains_non_english

# Example usage
sentence = "Hello World! Привет"
space, non_english = check_space_and_non_english(sentence)

print(f"Contains space: {space}")  # Output: True
print(f"Contains non-English letters: {non_english}")  # Output: True
