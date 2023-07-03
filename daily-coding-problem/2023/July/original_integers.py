"""
Daily Coding Problem: #755 (Easy) - Slack
Date: 07/03/2023

You are given a string formed by concatenating several words corresponding
to the integers zero through nine and then anagramming.

For example, the input could be 'niesevehrtfeev', which is an anagram of 'threefiveseven'.

Note that there can be multiple instances of each integer.

Given this string, return the original integers in sorted order. In the example above, this would be 357.
"""

# Algorith Used: Hash Table, String Manipulation, Sorting
# Time Complexity: O(n), where n is the length of the string
# Space Complexity: O(n), where n is the length of the string
def original_integers(string: str) -> int:
    """Return the original integers in sorted order from a string of anagrams of numbers.
    
    This solution uses a hash table to store the numbers and their corresponding letters.
    It then iterates through the hash table and removes the letters from the string.
    The remaining letters are the original integers in sorted order.

    The time complexity is O(n), where n is the length of the string, since 
    the algorithm iterates through the string once to remove the letters from the string.
    Note that the time complexity is not O(n^2) since the numbers hash table is a small constant.
    """

    # Hash table of numbers
    numbers = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    # Initialize string of letters
    string_letters = ""

    # Iterate through numbers
    for number in numbers:
        # Initialize current number
        current_number = number

        # Iterate through string
        for letter in string:
            # If letter is in current number, remove it
            if letter in number:
                current_number = current_number.replace(letter, '')

        # If current number is empty, add number to string of letters
        if current_number == '':
            for letter in number:
                string = string.replace(letter, '', 1)
            string_letters += numbers[number]
    
    # Return string of letters as an integer
    # Sorting is not necessary since the numbers are already in order in the hash table
    return int(string_letters)


if __name__ == "__main__":
    assert original_integers('niesevehrtfeev') == 357
