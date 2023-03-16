"""
Cracking the Coding Interview: 1.6

String Compression:
    - Implement a method to perform basic string compression using the counts of repeated characters.
    - For example, the string "aabcccccaaa" would become "a2b1c5a3".
    - If the "compressed" string would not become smaller than the original string, you method
      should return the original string.
    - You can assume the string has only uppercase and lowercase letters (a-z)
"""

# Algorithm Used: Iteration
# Time Complexity: O(n)
# Memory Complexity: O(n)
def stringCompression(original: str):

    # Create a variable for the new string and set it equal to the first character 
    # of the input string
    compressed = original[0]

    # Initialize a variable to keep count of the current consecutive occurs of a character
    currentCount = 0

    # Iterate through the input string
    # Update the count for the current consecutive occurrence
    # If the current character is the different than the previous, update the new string
    # and reset the current count
    for i in range(1, len(original)):
        currentCount += 1
        if original[i - 1] != original[i]:
            compressed += str(currentCount) 
            compressed += original[i]
            currentCount = 0

    # Remember to update the count after the last iteration
    compressed += str(currentCount + 1)

    # Return the compressed string if its smaller than the orginal string
    return compressed if len(compressed) < len(original) else original
