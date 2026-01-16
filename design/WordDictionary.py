"""
Design Add and Search Words Data Structure
https://leetcode.com/problems/design-add-and-search-words-data-structure/

Design a data structure that supports adding new words and
finding if a string matches any previously added string.

Implement the WordDictionary class:
    * WordDictionary()
        - Initializes the object.
    * void addWord(word)
        - Adds word to the data structure, it can be matched later.
    * bool search(word)
        - Returns true if there is any string in the data structure that matches word,
          false otherwise.
        - word may contain dots '.' where dots can be matched with any letter.

Example:
    * Input:
        - ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
        - [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
    * Output:
        - [null,null,null,null,false,true,true,true]

Explanation:
    * WordDictionary wordDictionary = new WordDictionary();
    * wordDictionary.addWord("bad");
    * wordDictionary.addWord("dad");
    * wordDictionary.addWord("mad");
    * wordDictionary.search("pad"); // return False
    * wordDictionary.search("bad"); // return True
    * wordDictionary.search(".ad"); // return True
    * wordDictionary.search("b.."); // return True

Constraints:
    * 1 <= word.length <= 25
    * word in addWord consists of lowercase English letters.
    * word in search consist of '.' or lowercase English letters.
    * There will be at most 2 dots in word for search queries.
    * At most 10^4 calls will be made to addWord and search.
"""


class Node:
    def __init__(self):
        self.children = [None for _ in range(26)]  #  26 possible children nodes (a-z)
        self.isEndOfWord = False                   # True if node represent the end of the word


class WordDictionary:
    def __init__(self):
        self.root = Node()

    def addWord(self, word: str):
        """Adds a word to the trie.
        
        Time Complexity: O(n), where n is the length of the word.

        Args:
            word: A string representing the word to add to the trie.

        Time Complexity:
            O(n), where n is the length of the word.
        """
        current = self.root

        for char in word:
            index = ord(char) - ord("a")
            if not current.children[index]:
                current.children[index] = Node()

            current = current.children[index]

        current.isEndOfWord = True

    def search(self, word: str) -> bool:
        """Searches (DFS) for a word in the trie.

        Time Complexity:
            O(n * 26) in the worst case, occurs when '.' appears.
            Otherwise O(n).
            Where n is the length of the word.

        Space Complexity:
            O(n), where n is the length of the word due to recursion stack usage.

        Args:
            word: A string representing the word to search for in the trie.

        Returns:
            A boolean indicating whether the word is in the trie.
        """
        return self.dfs(word, self.root)

    def dfs(self, word: str, node: Node) -> bool:
        """Depth First Search helper used to search a word in the trie.

        Args:
            word: A string representing the remaining portion of the word to search for.
            node: A Node object representing the current node in the trie.

        Returns:
            True if there is any string in the data structure that matches word, false otherwise.
        """
        current = node

        for i in range(len(word)):
            char = word[i]

            # If the character is '.', it can match any letter:
            #   Recursively search all possible child nodes.
            #   If any recursive call returns True, the word exists.
            if char == ".":
                for child in current.children:
                    if child and self.dfs(word[i + 1:], child):
                        return True
                return False

            # Get the index of the character in the alphabet:
            #   If the character does not exist in the trie, return False.
            index = ord(char) - ord("a")
            if not current.children[index]:
                return False

            # If the character exists in the trie, then update the current node to the next node.
            current = current.children[index]

        # At the end of the iteration, check if the current node is the end of the word.
        return current.isEndOfWord


if __name__ == "__main__":
    wordDictionary = WordDictionary()

    # Add words
    wordDictionary.addWord("bad")
    wordDictionary.addWord("dad")
    wordDictionary.addWord("mad")

    # Word searches
    assert wordDictionary.search("bad") is True
    assert wordDictionary.search("dad") is True
    assert wordDictionary.search("mad") is True
    assert wordDictionary.search("pad") is False

    # Wildcard searches
    assert wordDictionary.search(".ad") is True
    assert wordDictionary.search("b..") is True
    assert wordDictionary.search("..d") is True
    assert wordDictionary.search("...") is True
    assert wordDictionary.search("....") is False

    # Add more words
    wordDictionary.addWord("a")
    wordDictionary.addWord("ab")
    wordDictionary.addWord("ba")
    wordDictionary.addWord("abc")

    # New words searches
    assert wordDictionary.search("a") is True
    assert wordDictionary.search("ab") is True
    assert wordDictionary.search("abc") is True
    assert wordDictionary.search("abcd") is False
    assert wordDictionary.search("a.") is True
    assert wordDictionary.search(".") is True
    assert wordDictionary.search("..") is True
    assert wordDictionary.search("...") is True
    assert wordDictionary.search("....") is False

    # Mixed searches
    assert wordDictionary.search("a.c") is True
    assert wordDictionary.search("..c") is True
    assert wordDictionary.search(".b.") is True
    assert wordDictionary.search("b.") is True
