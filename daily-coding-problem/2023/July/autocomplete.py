"""
Daily Coding Problem: #11 (Medium) - Twitter
Date: 07/13/2023

Implement an autocomplete system.
That is, given a query string s and a set of all possible query strings, return all
strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal],
return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
"""

# Trie node
class Node:
    def __init__(self, val: str):
        self.val = val
        self.children = {}
        self.is_end = False


# Trie
class Trie:
    def __init__(self):
        self.root = Node('')

    def insert(self, word: str) -> None:
        """Insert a word into the trie

        Args:
            word (str): The word to insert

        Time Complexity:
            O(n), where n is the number of characters in the word

        Space Complexity:
            O(n), where n is the number of characters in the word
        """
        # Initialize the current node to the root
        curr = self.root

        # Iterate through the word
        for char in word:
            # If the current character is not in the trie, add it
            if char not in curr.children:
                curr.children[char] = Node(char)
        
            # Update the current node
            curr = curr.children[char]

        # Mark the end of the word
        curr.is_end = True

    def starts_with(self, prefix: str) -> list:
        """Check if the trie starts with the prefix

        Args:
            prefix (str): The prefix to check

        Time Complexity:
            O(n), where n is the number of characters in the prefix

        Space Complexity:
            O(n), where n is the number of characters in the prefix

        Returns:
            bool: True if the trie starts with the prefix, False otherwise
        """
        # Initialize the current node to the root
        words = []
        curr = self.root

        # Iterate through the prefix
        for char in prefix:
            # If the current character is not in the trie, return False
            if char not in curr.children:
                return words
            
            # Update the current node
            curr = curr.children[char]

        # Recursively get the words that start with the prefix
        def get_words(node: Node, word: str) -> None:
            # Base case (node is the end of a word)
            if node.is_end:
                words.append(word)
            
            # Recursive case (node is not the end of a word)
            for child in node.children:
                get_words(node.children[child], word + child)

        # Get the words that start with the prefix
        get_words(curr, prefix)

        # Return the words that start with the prefix
        return words
        

# Algorithm Used: Trie
# Time Complexity: O(n), where n is the number of characters in the query string
# Space Complexity: O(n), where n is the number of characters in the query string
def autocomplete(query: str, words: list) -> list:
    # Initialize the trie
    trie = Trie()

    # Insert the words into the trie
    for word in words:
        trie.insert(word)

    # Return the words that start with the query string
    return trie.starts_with(query)


if __name__ == '__main__':
    assert autocomplete('de', ['dog', 'deer', 'deal']) == ['deer', 'deal']
    assert autocomplete('do', ['dog', 'deer', 'deal']) == ['dog']
    assert autocomplete('d', ['dog', 'deer', 'deal']) == ['dog', 'deer', 'deal']
    assert autocomplete('e', ['dog', 'deer', 'deal']) == []
    print('Passed all tests.')