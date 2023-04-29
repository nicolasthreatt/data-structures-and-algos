"""
https://leetcode.com/problems/design-add-and-search-words-data-structure/

Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:
    * WordDictionary()
        - Initializes the object.
    * void addWord(word)
        - Adds word to the data structure, it can be matched later.
    * bool search(word)
        - Returns true if there is any string in the data structure that matches word or false otherwise.
          word may contain dots '.' where dots can be matched with any letter.

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


class TrieNode:
    """Trie node class.

    Attributes:
        children: A list of TrieNode objects (26 nodes represententing a-z).
        isEndofWord: A boolean indicating whether the node is the end of a word.
    """

    def __init__(self) -> None:
        # Create a list to store the children nodes for the 26 possible children nodes (a-z).
        self.children = [None for _ in range(26)]

        # isEndOfWord is True if node represent the end of the word
        self.isEndOfWord = False


class WordDictionary:
    """WordDictionary class.

    Attributes:
        root: A TrieNode object representing the root of the trie.

    """

    def __init__(self):
        """Initialize the root node of the trie.

        Time Complexity:
            O(1), constant time for the 26 elements in the list.

        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """Adds a word to the trie.

        Args:
            word: A string representing the word to add to the trie.

        Time Complexity:
            O(n), where n is the length of the word.
        """
        current = self.root

        for char in word:
            index = ord(char) - ord("a")
            if not current.children[index]:
                current.children[index] = TrieNode()

            current = current.children[index]

        current.isEndOfWord = True

    def search(self, word: str) -> bool:
        """Searches for a word in the trie."""
        return self.searchHelper(word, self.root)

    def searchHelper(self, word: str, node: TrieNode) -> bool:
        """Helper function for search.

        Args:
            word: A string representing the word to search for in the trie.
            node: A TrieNode object representing the current node in the trie.

        Returns:
            A boolean indicating whether the word is in the trie.
        """
        current = node

        for i in range(len(word)):
            char = word[i]
            if char == ".":
                for child in current.children:
                    if child and self.searchHelper(word[i + 1 :], child):
                        return True
                return False

            index = ord(char) - ord("a")
            if not current.children[index]:
                return False

            current = current.children[index]

        return current.isEndOfWord
